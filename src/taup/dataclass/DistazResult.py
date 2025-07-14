from dataclasses import dataclass, field

from .Daz import Daz

@dataclass
class DistazResult:
    calctype: str
    invflattening: float
    sources: list
    receivers: list
    radius: float|None = None
    model: str|None = None
    distances: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = DistazResult(
            jsonObj['calctype'],
            jsonObj['invflattening'],
            jsonObj['sources'],
            jsonObj['receivers'],
            )
        if "radius" in jsonObj:
            res.radius = jsonObj['radius']
        if "model" in jsonObj:
            res.model = jsonObj['model']
        for d in jsonObj['distances']:
            res.distances.append(Daz.from_json(d))
        return res
