from dataclasses import dataclass, field, asdict

from .CurveSegment import CurveSegment


@dataclass
class Curve:
    label: str
    description: str
    x: str
    y: str
    segments: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj) -> "Curve":
        res = Curve(
            jsonObj["label"], jsonObj["description"], jsonObj["x"], jsonObj["y"]
        )
        for s in jsonObj["segments"]:
            res.segments.append(CurveSegment.from_json(s))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
