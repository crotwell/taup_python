#!/usr/bin/env python

import taup

eventLatLon = [35, -50]
staLatLons = [ [34, -80], [35, -81]]


with taup.TauPServer() as taupserver:

    # query params correspond to the tools, may be any one of:
    # Time, Pierce, Path, Curve, Discon, Distaz, Find, Phase,
    # Refltrans, Table, Velmerge, Velplot, Version, Wavefront
    params = taup.BeachballQuery()
    # params that will stay the same can be reused
    params.phase(["S","pS"])
    params.model('ak135')
    params.strikediprake(35, 45, -75)
    params.hemi('both')

    params.event( *eventLatLon ) # splat to expand list into function args
    params.sourcedepth([100])
    for sta in staLatLons:
        params.andStation( *sta )

    # calculate results, parsed as JSON and returned as dataclass objects
    bbResult = params.calc(taupserver)
    print("Arrivals: takeoff, azimuth, phase, PSv, Sh")
    print("--------------------------------")
    for a in bbResult.arrivals:
        print(f"Arr: {a.takeoff:8.3f} {a.azimuth:8.3f} {a.phase} {a.amp.factorpsv} {a.amp.factorsh}")
    print()
    print("Radiation Pattern: takeoff, azimuth, P, Sv, Sh")
    print("----------------------------------------------")
    for rp in bbResult.radiationPattern:
        print(" ".join(f"{x:8.3f}" for x in rp))
