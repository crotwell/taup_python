#!/usr/bin/env python

import taup

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer(verbose=True) as taupserver:

    # query params correspond to the tools, one of:
    # time, pierce, path, curve, discon, distaz, find, phase, refltrans, table, velplot, wavefront
    params = taup.PierceQuery()
    # params that will stay the same
    params.phase(["P", "S"])
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
        pierceResult = params.calc(taupserver)
        for a in pierceResult.arrivals:
            print(f"{a.phase}   {a.sourcedepth} {a.distdeg} {a.time}  {a.desc if a.desc is not None else ''} p: {len(a.pierce)}")
            if a.pierce is not None:
                print(f"Pierce:")
                for td in a.pierce:
                    print(f"  {td}")
            else:
                print("No Pierce")
