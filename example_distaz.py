#!/usr/bin/env python

import taup

with taup.TauPServer() as taupserver:

    # query params correspond to the tools, may be any one of:
    # Time, Pierce, Path, Curve, Discon, Distaz, Find, Phase,
    # Refltrans, Table, Velmerge, Velplot, Version, Wavefront
    params = taup.DistazQuery()
    # params that will stay the same can be reused
    params.geodetic(True)


    eventLatLons = [ [35, -50], [-29, 45]]
    staLatLons = [ [34, -80], [35, -81]]

    for sta in staLatLons:
        params.station( *sta )
        for evt in eventLatLons:
            params.event( *evt )
            # calculate results, parsed as JSON and returned as dataclass objects
            distazResult = params.calc(taupserver)
            if distazResult.calctype == "geodetic":
                print(f"    geodetic, flattening= 1/{distazResult.invflattening}")
            for d in distazResult.distances:
                km = f"Km: {d.km}" if d.km is not None else ""
                print(f"from {sta} to {evt}: Dist: {d.deg} Az: {d.az} Baz: {d.baz} {km}")
