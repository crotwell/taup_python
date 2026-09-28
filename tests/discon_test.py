import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPDiscon:

    def testDataClass(self, taupserver):
        params = taup.DisconQuery()
        params.model('ak135fcont')
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.DisconResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)
        # dataclass to dict
        jsonMatchDataclass(ans.__dict__, ans)
