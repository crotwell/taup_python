import taup
import requests

with taup.TauPServer("../TauP/build/install/TauP/bin/taup") as timeserver:
    timeParams = taup.TimeQuery()
    timeParams.phase = ["P", "S"]
    timeParams.event = [35, -50]
    timeParams.sid = ["CO_HAW", "CO_BIRD"]
    timeParams.evdepth = [100]
    timeParams.model = 'ak135'

    jsonTimes = timeParams.calc(timeserver)
    if len(jsonTimes["arrivals"]) == 0:
        print("No arrivals...")
    else:
        print("Phase Depth    Dist  Time")
    for a in jsonTimes["arrivals"]:
        print(f"{a['phase']}   {a['sourcedepth']} {a['distdeg']} {a['time']}  {a['desc']}")
