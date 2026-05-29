import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPFind:

    def testDataClass(self, taupserver):
        params = taup.FindQuery()
        params.max(1)
        params.amp()
        params.az(35)
        params.model('ak135fcont')
        params.strikediprake(35, 65, 75)
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.FindResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)