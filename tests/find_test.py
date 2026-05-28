import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPFind:

    def testDataClass(self, taupserver):
        params = taup.FindQuery()
        params.amp()
        params.az(35)
        params.model('ak135fcont')
        params.event( 35, -50 )
        params.sourcedepth([100])
        params.station( 34, -80 )
        params.strikediprake(35, 65, 75)
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.FindResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)