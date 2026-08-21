#!/usr/bin/env python

import taup
import json

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
    params.hemi('lower')
    params.numpoints(50)

    params.event( *eventLatLon ) # splat to expand list into function args
    params.sourcedepth([100])
    for sta in staLatLons:
        params.andStation( *sta )

    # calculate results, parsed as JSON and returned as dataclass objects
    bbResult = params.calc(taupserver)
    for bb in bbResult.beachballs:
        npt = bb.nptAxis
        print("Axis: Takeoff  Azimuth")
        print("----------------------")
        print(f"N: {npt.n.takeoff:8.2f}  {npt.n.azimuth:8.2f}")
        print(f"P: {npt.p.takeoff:8.2f}  {npt.p.azimuth:8.2f}")
        print(f"T: {npt.t.takeoff:8.2f}  {npt.t.azimuth:8.2f}")
        print()
        print("Arrivals:")
        print("    Takeoff, Azimuth, Phase, PSv, Sh")
        print("----------------------------------------------")
        for a in bb.arrivals:
            print(f"    {a.takeoff:8.2f} {a.azimuth:8.2f}   {a.phase}   {a.amp.factorpsv:.1e} {a.amp.factorsh:.1e}")
        print()
        print(f"Radiation Pattern: ({params.get_hemi()})")
        print("   Takeoff  Azimuth      P      Sv      Sh")
        print("----------------------------------------------")
        for rp in bb.radiationPattern:
            print(" ".join(f"{x:8.2f}" for x in rp))
