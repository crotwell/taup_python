#!/usr/bin/env python

import taup

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer() as taupserver:

    # query params correspond to the tools, may be any one of:
    # Time, Pierce, Path, Curve, Discon, Distaz, Find, Phase,
    # Refltrans, Table, Velmerge, Velplot, Version, Wavefront
    params = taup.TimeQuery()
    # params that will stay the same can be reused
    params.phase(["S","PedoS"])
    params.model('ak135')
    params.geodetic(True)
    params.scatter(500, 2)
    params.rel("P")

    # params that will vary
    for event in eventLatLons:
        params.event( *event ) # splat to expand list into function args
        params.sourcedepth([100])
        for sta in staLatLons:
            params.station( *sta )

            # calculate results, parsed as JSON and returned as dataclass objects
            timeResult = params.calc(taupserver)
            if len(timeResult.arrivals) == 0:
                print(f"No arrivals...{event} to {sta}")
            else:
                print("Phase Depth    Dist  Time   Desc")
            for a in timeResult.arrivals:
                #print(a)
                print(f"{a.phase}   {a.sourcedepth} {a.distdeg} {a.time}  {a.desc}")
                if a.relative:
                    print(f"    Relative: {a.phase} - {a.relative.arrival.phase} = {a.relative.difference} s")
