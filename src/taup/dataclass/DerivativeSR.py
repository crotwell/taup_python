from dataclasses import dataclass, asdict

@dataclass
class DerivativeSR:
    velocity: float
    radialslowness: float
    radius: float

    @classmethod
    def from_json(cls, jsonObj) -> 'DerivativeSR':
        return DerivativeSR(
            jsonObj['velocity'],
            jsonObj['radialslowness'],
            jsonObj['radius']
            )

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
