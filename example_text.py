import taup
import requests

eventLatLons = [ [35, -50], [-29, 45]]
staLatLons = [ [34, -80], [35, -81]]

print("IN TEXT")
with taup.TauPServer() as taupserver:

    timeParams = taup.PathQuery()
    # params that will stay the same
    timeParams.phase(["P", "S"])
    timeParams.model('ak135')
    timeParams.geodetic(True)

    timeParams.event( *eventLatLons[0] )
    timeParams.sourcedepth([100])
    for sta in staLatLons:
        timeParams.andStation( *sta )

    #textTimes = timeParams.queryText(timeserver)
    textTimes = timeParams.calcGmt(taupserver)
    print(textTimes)
