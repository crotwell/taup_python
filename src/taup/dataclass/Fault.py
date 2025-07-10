from dataclasses import dataclass

@dataclass
class Fault:
    strike: float
    dip: float
    rake: float

    @classmethod
    def from_json(cls, jsonObj):
        return Fault(jsonObj['strike'],jsonObj['dip'],jsonObj['rake'])
