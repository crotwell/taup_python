from dataclasses import dataclass, field

from .Daz import Daz
from .DistCalcType import DistCalcType
from .LatLonDepth import LatLonDepth

@dataclass
class DistazResult:
    disttypes: list = field(default_factory=list)
    sources: list = field(default_factory=list)
    receivers: list = field(default_factory=list)
    model: str|None = None
    distances: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = DistazResult()
        if "model" in jsonObj:
            res.model = jsonObj['model']
        for s in jsonObj['sources']:
            res.sources.append(LatLonDepth.from_json(s))
        for r in jsonObj['receivers']:
            res.receivers.append(LatLonDepth.from_json(r))
        for d in jsonObj['distances']:
            res.distances.append(Daz.from_json(d))
        for d in jsonObj['disttypes']:
            res.disttypes.append(DistCalcType.from_json(d))
        return res
