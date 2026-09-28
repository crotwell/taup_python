from dataclasses import dataclass, field, asdict

@dataclass
class PhaseRay:
    dist: float
    modulodist: float
    rayparameter: float
    time: float

    @classmethod
    def from_json(cls, jsonObj) -> 'PhaseRay':
        res = PhaseRay(
            jsonObj['dist'],
            jsonObj['modulodist'],
            jsonObj['rayparameter'],
            jsonObj['time']
            )
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
