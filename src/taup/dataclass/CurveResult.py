from dataclasses import dataclass, field

from .Scatter import Scatter
from .Curve import Curve

@dataclass
class CurveResult:
    model: str
    sourcedepthlist: list
    receiverdepthlist: list
    phases: list
    scatter: Scatter = None
    curves: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = CurveResult(
            jsonObj['model'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases']
            )
        if 'scatter' in jsonObj:
            res.scatter = Scatter.from_json(jsonObj['scatter'])
        for c in jsonObj['curves']:
            res.curves.append(Curve.from_json(c))
        return res
