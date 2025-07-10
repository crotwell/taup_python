from dataclasses import dataclass, field

from .Arrival import Arrival
from .Scatter import Scatter

@dataclass
class TimeResult:
    model: str
    sourcedepthlist: list
    receiverdepthlist: list
    phases: list
    scatter: Scatter = None
    arrivals: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = TimeResult(
            jsonObj['model'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases']
            )
        if 'scatter' in jsonObj:
            res.scatter = Scatter.from_json(jsonObj['scatter'])
        for arr in jsonObj['arrivals']:
            res.arrivals.append(Arrival.from_json(arr))
        return res
