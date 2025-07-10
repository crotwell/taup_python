from dataclasses import dataclass, field

from .TimeDist import TimeDist

@dataclass
class PathSegment:
    name: str
    wavetype: str
    segment: list[list[TimeDist]] = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        ps = PathSegment(jsonObj['name'], jsonObj['wavetype'])
        for p in jsonObj['segment']:
            ps.segment.append(TimeDist.from_json(p))
        return ps
