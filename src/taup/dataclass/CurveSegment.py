from dataclasses import dataclass, field

@dataclass
class CurveSegment:
    x: list = field(default_factory=list)
    y: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        return CurveSegment(
            jsonObj['x'],
            jsonObj['y']
            )
