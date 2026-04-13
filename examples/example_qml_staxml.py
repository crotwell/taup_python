#!/usr/bin/env python

import taup

with taup.TauPServer(verbose=True) as taupserver:
    params = taup.TimeQuery()
    params.model("prem")
    params.phase(["P", "S"])
    # must read quakeml and stationxml files, then send the text
    # rather than just send the filename
    with open("my_midatlantic.qml", "r") as inqml:
        params.quakemltext(inqml.read())
    #params.deg(35)
    with open("my_stations.staml", "r") as instaxml:
        params.staxmltext(instaxml.read())
    params.amp()
    taupResult = params.calc(taupserver)
    if len(taupResult.arrivals) == 0:
        print(f"No arrivals...")
    else:
        print(f"{'Phase':^10}  {'Depth':^10}  {'Dist':^10}  {'Time':^10}  {'AmpPSv':^8}  {'AmpSh':^8}")
        for a in taupResult.arrivals:
            print(f"{a.phase:>10}  {a.sourcedepth:>10}  {a.distdeg:>10.3f}  {a.time:>10.3f}  {a.amp.factorpsv:0.1e}  {a.amp.factorsh:0.1e}  \"{a.desc}\"")
