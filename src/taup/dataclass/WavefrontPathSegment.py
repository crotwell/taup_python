from dataclasses import dataclass, field, asdict

from .TimeDist import TimeDist


@dataclass
class WavefrontPathSegment:
    name: str
    wavetype: str
    segment: list[TimeDist] = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj) -> "WavefrontPathSegment":
        ps = WavefrontPathSegment(jsonObj["name"], jsonObj["wavetype"])
        for p in jsonObj["segment"]:
            ps.segment.append(TimeDist.from_json(p))
        return ps

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
