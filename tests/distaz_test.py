import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPBeachball:

    def testDataClass(self, taupserver):
        
        params = taup.DistazQuery()
        # params that will stay the same can be reused
        params.geodist(["spherical", "geocentric", "geodetic"])


        eventLatLons = [ [35, -50], [-29, 45]]
        staLatLons = [ [34, -80], [35, -81]]

        params.station( *staLatLons[0] )
        params.event( *eventLatLons[0] )
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.DistazResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)