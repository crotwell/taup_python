from dataclasses import dataclass, field

from .Curve import Curve
from .VelocityDiscontinuity import VelocityDiscontinuity

@dataclass
class ReflTransResult:


    fsrf: bool = False
    downgoing: bool = False

    incidentwave: list = field(default_factory=list)

    discon: VelocityDiscontinuity|None=None

    model: str|None = None

    discondepth: float|None = None
    disconname: str|None = None

    curves: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = ReflTransResult(
            jsonObj['fsrf'],
            jsonObj['downgoing']
            )
        if 'discondepth' in jsonObj:
            res.discondepth = jsonObj['discondepth']
        if 'disconname' in jsonObj:
            res.disconname = jsonObj['disconname']
        if 'model' in jsonObj:
            res.model = jsonObj['model']
        res.discon = VelocityDiscontinuity.from_json(jsonObj["discon"])
        for w in jsonObj['incidentwave']:
            res.incidentwave.append(w)
        for c in jsonObj['curves']:
            res.curves.append(Curve.from_json(c))
        return res
