#!/usr/bin/env python

import taup
import requests

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer() as taupserver:


    # query params correspond to the tools, may be any one of:
    # Time, Pierce, Path, Curve, Discon, Distaz, Find, Phase,
    # Refltrans, Table, Velmerge, Velplot, Version, Wavefront
    params = taup.CurveQuery()
    # params that will stay the same can be reused
    params.phase(["S","PedoS"])
    params.model('ak135')
    params.scatter(500, 2)
    params.rel("P")


    # calculate results, parsed as JSON and returned as dataclass objects
    jsonCurve = params.calc(taupserver)
    for c in jsonCurve.curves:
        print(f"curve {c.label} is {c.description}")
