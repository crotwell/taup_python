from dataclasses import dataclass, field

@dataclass
class PhaseRay:
    dist: float
    modulodist: float
    rayparameter: float
    time: float

    @classmethod
    def from_json(cls, jsonObj):
        res = PhaseRay(
            jsonObj['dist'],
            jsonObj['modulodist'],
            jsonObj['rayparameter'],
            jsonObj['time']
            )
        return res
