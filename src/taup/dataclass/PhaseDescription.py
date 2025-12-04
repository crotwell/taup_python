from dataclasses import dataclass, field
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
    def from_json(cls, jsonObj):
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
