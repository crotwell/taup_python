from dataclasses import dataclass, field, asdict
from .PhaseRay import PhaseRay
from .PhaseSegment import PhaseSegment


@dataclass
class PhaseDescription:
    name: str
    puristname: str
    sourcedepth: float
    receiverdepth: float
    fail: str|None = None
    minexists: PhaseRay|None = None
    maxexists: PhaseRay|None = None
    shadow: list = field(default_factory=list)
    segments: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj) -> 'PhaseDescription':
        res = PhaseDescription(
            jsonObj['name'],
            jsonObj['puristname'],
            jsonObj['sourcedepth'],
            jsonObj['receiverdepth']
            )
        if 'fail' in jsonObj:
            res.fail = jsonObj['fail']
        else:
            res.minexists = PhaseRay.from_json(jsonObj['minexists'])
            res.maxexists = PhaseRay.from_json(jsonObj['maxexists'])
            for seg in jsonObj['segments']:
                res.segments.append(PhaseSegment.from_json(seg))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
