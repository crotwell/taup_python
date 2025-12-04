
from dataclasses import dataclass, field
from .PhaseDescription import PhaseDescription
from .Scatter import Scatter


@dataclass
class PhaseResult:
    model: str
    sourcedepthlist: list
    receiverdepthlist: list
    phases: list
    scatter: Scatter = None
    descriptions: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = PhaseResult(
            jsonObj['model'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases']
            )
        if 'scatter' in jsonObj:
            res.scatter = Scatter.from_json(jsonObj['scatter'])
        for arr in jsonObj['descriptions']:
            res.descriptions.append(PhaseDescription.from_json(arr))
        return res
