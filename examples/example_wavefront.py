#!/usr/bin/env python

import taup
import requests

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer() as taupserver:


    # query params correspond to the tools, may be any one of:
    # Time, Pierce, Path, Curve, Discon, Distaz, Find, Phase,
    # Refltrans, Table, Velmerge, Velplot, Version, Wavefront
    params = taup.WavefrontQuery()
    # params that will stay the same can be reused
    params.phase(["S","PedoS"])
    params.model('ak135')
    params.scatter(500, 2)


    # calculate results, parsed as JSON and returned as dataclass objects
    jsonWavefront = params.calc(taupserver)
    for c in jsonWavefront.isochrons:
        print(f"wavefront at {c.time} has {len(c.wavefronts)} phases")
        for w in c.wavefronts:
            print(f"    {w.phase} has {len(w.segments)} segments")
