from dataclasses import dataclass, field

from .WavefrontPathSegment import WavefrontPathSegment

@dataclass
class Wavefront:
    time: float
    phase: str
    model: str
    sourcedepth: float
    receiverdepth: float
    segments: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = Wavefront(
            jsonObj['time'],
            jsonObj['phase'],
            jsonObj['model'],
            jsonObj['sourcedepth'],
            jsonObj['receiverdepth']
            )
        for s in jsonObj['segments']:
            res.segments.append(WavefrontPathSegment.from_json(s))
        return res
