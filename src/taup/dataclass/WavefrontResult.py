from dataclasses import dataclass, field, asdict

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
    def from_json(cls, jsonObj) -> 'WavefrontResult':
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

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
