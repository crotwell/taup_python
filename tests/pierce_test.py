import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPPierce:
    def test_amp(self, taupserver):
        eventLatLons = [ [35, -50], [-29, 45]]
        staLatLons = [ [34, -80], [35, -81]]
        params = taup.PierceQuery()
        params.phase(["S","P"])
        params.model('ak135fcont')
        params.amp()
        params.event( *eventLatLons[0] ) # splat to expand list into function args
        params.sourcedepth([100])
        for sta in staLatLons:
            params.station( *sta )
        ans = params.calc(taupserver)
        assert len(ans.arrivals) > 0
        assert getattr(ans.arrivals[0], 'pierce') is not None 

    def testDataClass(self, taupserver):

        params = taup.PierceQuery()
        params.phase(["S","P"])
        params.model('ak135fcont')
        params.amp()
        params.event( 35, -50 )
        params.sourcedepth([100])
        params.station( 34, -80 )
        jsonAns = params.calcJson(taupserver)
        # pierce uses TimeResult
        ans = taup.dataclass.TimeResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)

