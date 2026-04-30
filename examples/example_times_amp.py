#!/usr/bin/env python

import taup
import requests

staLatLons = [ [34, -80], [35, -81]]


with taup.TauPServer() as taupserver:
    params = taup.TimeQuery()
    # params that will stay the same can be reused
    params.phase(["SKS","SKKS"])
    params.model('ak135fcont')
    params.geodist('geodetic')
    params.amp()
    params.strikediprake([35, 75, 90])
    params.mw(6)
    params.event(-29, 45)
    params.sourcedepth([100])


    # params that will vary

    for sta in staLatLons:
        params.station( *sta )

        # calculate results, parsed as JSON and returned as dataclass objects
        jsonTimes = params.calc(taupserver)
        if len(jsonTimes.arrivals) == 0:
            print(f"No arrivals... at {sta}")
        else:
            print("Phase Depth    Dist    Time     Amp      Desc")
        for a in jsonTimes.arrivals:
            #print(a)
            print(f"{a.phase}   {a.sourcedepth} {a.distdeg} {a.time}  {a.amp.factorpsv:.1e}  {a.desc}")
            if len(a.pierce) != 0:
                print("Pierce:")
                for p in a.pierce:
                    print(f"  {p}")
            if a.relative:
                print(f"    Relative: {a.phase} - {a.relative.arrival.phase} = {a.relative.difference} s")
