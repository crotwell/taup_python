from dataclasses import dataclass

@dataclass
class DerivativeSR:
    velocity: float
    radialslowness: float
    radius: float

    @classmethod
    def from_json(cls, jsonObj):
        return DerivativeSR(
            jsonObj['velocity'],
            jsonObj['radialslowness'],
            jsonObj['radius']
            )
