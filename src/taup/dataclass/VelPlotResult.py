from dataclasses import dataclass, field, asdict
from .Curve import Curve


@dataclass
class VelPlotResult:
    x: str
    y: str
    modelnames: list = field(default_factory=list)
    curves: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj) -> "VelPlotResult":
        res = VelPlotResult(jsonObj["x"], jsonObj["y"])
        for m in jsonObj["modelnames"]:
            res.modelnames.append(m)
        for c in jsonObj["curves"]:
            res.curves.append(Curve.from_json(c))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
