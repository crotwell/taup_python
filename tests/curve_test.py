import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPCurve:

    def testDataClass(self, taupserver):
        params = taup.CurveQuery()
        # params that will stay the same can be reused
        params.phase(["S","PedoS"])
        params.model('ak135')
        params.scatter(500, 2)
        params.rel("P")


        # calculate results, parsed as JSON and returned as dataclass objects
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.CurveResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)