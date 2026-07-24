import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPRefltrans:

    def testDataClass(self, taupserver):
        params = taup.RefltransQuery()
        params.model('ak135fcont')
        params.depth(410)
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.ReflTransResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)