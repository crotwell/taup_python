from dataclasses import dataclass, asdict


@dataclass
class Fault:
    strike: float
    dip: float
    rake: float

    @classmethod
    def from_json(cls, jsonObj) -> "Fault":
        return Fault(jsonObj["strike"], jsonObj["dip"], jsonObj["rake"])

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
