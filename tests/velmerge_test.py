import pytest
import taup
from .conftest import taupserver, jsonMatchDataclass

class TestTauPVelMerge:

    def testDataClass(self, taupserver):
        params = taup.VelmergeQuery()
        params.model("iasp91")
        jsonAns = params.calcJson(taupserver)
        ans = taup.dataclass.VelocityModel.from_json(jsonAns)
        jsonMatchDataclass(jsonAns, ans)
