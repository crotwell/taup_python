from dataclasses import dataclass, field, asdict


@dataclass
class CurveSegment:
    x: list = field(default_factory=list)
    y: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj) -> "CurveSegment":
        return CurveSegment(jsonObj["x"], jsonObj["y"])

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
