from dataclasses import dataclass, field

from .Scatter import Scatter
from .Isochron import Isochron

@dataclass
class WavefrontResult:
    model: str
    sourcedepthlist: list
    receiverdepthlist: list
    phases: list
    timesteps: list
    scatter: Scatter|None = None
    isochrons: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = WavefrontResult(
            jsonObj['model'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases'],
            jsonObj['timesteps']
            )
        if 'scatter' in jsonObj:
            res.scatter = Scatter.from_json(jsonObj['scatter'])
        for c in jsonObj['isochrons']:
            res.isochrons.append(Isochron.from_json(c))
        return res
