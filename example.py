import taup
import requests

with taup.TauPServer() as taup:

    #####################################################
    # now repeated process earthquakes, distances, etc...

    # list of distances to the stations, lets be crazy and do all 0,1,2,...,180 degrees
    deglist = ",".join(str(d) for d in range(181))
    print("deglist")
    print(deglist)

    # loop over depths. Alternatively, we could send in one huge request
    # for all the depths, but more complex to deal with the reaults if too big
    for eqdepth in range(0, 500, 100):
        for degree in range(10,181,30):
            deglist = degree
            print(f"depth= {eqdepth} deg={degree}")
            params = {
                'model':'ak135',
                'evdepth':eqdepth,
                'phase':'P,S',
                'degree':deglist,
                'format':'json'
            }

            jsonTimes = taup.queryJson(params)
            if len(jsonTimes["arrivals"]) == 0:
                print("No arrivals...")
            for a in jsonTimes["arrivals"]:
                print(f"{a['phase']} {a['sourcedepth']} {a['distdeg']} {a['time']}")
