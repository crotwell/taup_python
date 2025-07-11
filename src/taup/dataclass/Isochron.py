from dataclasses import dataclass, field

from .Wavefront import Wavefront

@dataclass
class Isochron:
    time: float
    wavefronts: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = Isochron(
            jsonObj['time']
            )
        for s in jsonObj['wavefronts']:
            res.wavefronts.append(Wavefront.from_json(s))
        return res
