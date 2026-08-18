import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPVelPlot:

    def testDataClass(self, taupserver):
        params = taup.VelplotQuery()
        params.model(["iasp91", "prem"])
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.VelPlotResult.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)
