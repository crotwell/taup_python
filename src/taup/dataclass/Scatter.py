from dataclasses import dataclass, asdict

@dataclass
class Scatter:
    depth: float
    distdeg: float

    @classmethod
    def from_json(cls, jsonObj) -> 'Scatter':
        return Scatter(
            jsonObj['depth'],
            jsonObj['distdeg'])

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
