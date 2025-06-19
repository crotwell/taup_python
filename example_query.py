import taup
import requests

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

with taup.TauPServer("../TauP/build/install/TauP/bin/taup") as timeserver:

    timeParams = taup.TimeQuery()
    # params that will stay the same
    timeParams.phase(["P", "S"])
    timeParams.model('ak135')
    timeParams.geodetic(True)

    # params that will vary
    for event in eventLatLons:
        timeParams.event(event)
        timeParams.sourcedepth([100])
        for sta in staLatLons:
            timeParams.station(sta)

            jsonTimes = timeParams.calc(timeserver)
            if len(jsonTimes["arrivals"]) == 0:
                print(f"No arrivals...{event} to {sta}")
            else:
                print("Phase Depth    Dist  Time")
            for a in jsonTimes["arrivals"]:
                desc= a['desc'] if "desc" in a else ""
                #print(a)
                print(f"{a['phase']}   {a['sourcedepth']} {a['distdeg']} {a['time']}  {desc}")
