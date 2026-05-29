import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPPhase:

    def testDataClass(self, taupserver):
        params = taup.PhaseQuery()
        params.phase(["P", "S"])
        params.sourcedepth(35)
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.PhaseResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)