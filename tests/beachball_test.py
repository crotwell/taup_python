import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPBeachball:

    def testDataClass(self, taupserver):
        params = taup.BeachballQuery()
        params.phase(["S","P"])
        params.model('ak135fcont')
        params.event( 35, -50 )
        params.sourcedepth([100])
        params.station( 34, -80 )
        params.strikediprake(35, 65, 75)
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.BeachballResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)