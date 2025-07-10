#!/usr/bin/env python

import taup
import requests

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer() as timeserver:

    # query params correspond to the tools, one of:
    # time, pierce, path, curve, discon, distaz, find, phase, refltrans, table, velplot, wavefront
    timeParams = taup.TimeQuery()
    # params that will stay the same
    timeParams.phase(["P", "S"])
    timeParams.model('ak135')
    timeParams.geodetic(True)

    # params that will vary
    for event in eventLatLons:
        timeParams.event( *event ) # splat to expand list into function args
        timeParams.sourcedepth([100])
        for sta in staLatLons:
            timeParams.station( *sta )

            # calculate results, parsed as JSON and returned as dict
            jsonTimes = timeParams.calc(timeserver)
            if len(jsonTimes.arrivals) == 0:
                print(f"No arrivals...{event} to {sta}")
            else:
                print("Phase Depth    Dist  Time")
            for a in jsonTimes.arrivals:
                #print(a)
                print(f"{a.phase}   {a.sourcedepth} {a.distdeg} {a.time}  {a.desc}")
