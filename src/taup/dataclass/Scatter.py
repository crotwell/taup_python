from dataclasses import dataclass

@dataclass
class Scatter:
    depth: float
    distdeg: float

    @classmethod
    def from_json(cls, jsonObj):
        return Scatter(
            jsonObj['depth'],
            jsonObj['distdeg'])
