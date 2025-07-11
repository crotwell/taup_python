#!/usr/bin/env python

import taup
import requests

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer() as taupserver:

    # query params correspond to the tools, may be any one of:
    # Time, Pierce, Path, Curve, Discon, Distaz, Find, Phase,
    # Refltrans, Table, Velmerge, Velplot, Version, Wavefront
    params = taup.TimeQuery()
    params.phase(["P", "S"])
    params.model('ak135')
    params.geodetic(True)

    params.event( *eventLatLons[0] )
    params.sourcedepth([100])
    for sta in staLatLons:
        params.andStation( *sta )

    # get result as text, or other format depending on the tool, like:
    # calcGmt, calcSvg, calcJson, calcCsv...
    textResult = params.calcText(taupserver)
    print(textResult)
