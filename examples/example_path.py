#!/usr/bin/env python

import taup

eventLatLons = [ [-35, -50], ]
staLatLons = [  [35, -81]]

with taup.TauPServer() as taupserver:

    # query params correspond to the tools, one of:
    # time, pierce, path, curve, discon, distaz, find, phase, refltrans, table, velplot, wavefront
    params = taup.PathQuery()
    # params that will stay the same
    params.phase(["P", "SKS"])
    params.model('ak135')
    params.geodetic(True)

    params.event( *eventLatLons[0] )
    params.sourcedepth([100])
    for sta in staLatLons:
        params.station( *sta )

        # get result as text, or other format depending on the tool, like:
        # gmt, svg, json, csv...
        #textResult = params.calcSvg(taupserver)
        #print(textResult)
        # or
        #textResult = params.calcGmt(taupserver)
        #print(textResult)
        # or
        pathResult = params.calc(taupserver)
        for a in pathResult.arrivals:
            print(f"{a.phase}   {a.sourcedepth} {a.distdeg} {a.time}  {a.desc if a.desc is not None else ''}")
            if a.pathlength is not None:
                print(f"  Path length: {a.pathlength} km")
            else:
                print("  No Path")
            for pathseg in a.path:
                firstPoint = pathseg.segment[0]
                lastPoint = pathseg.segment[-1]
                print(f"    {pathseg.name} as {pathseg.wavetype} from {firstPoint.depth} km at {firstPoint.distdeg} deg to {lastPoint.depth} km at {lastPoint.distdeg} deg takes {lastPoint.time-firstPoint.time} sec")
