from dataclasses import dataclass
from .DerivativeSR import DerivativeSR

@dataclass
class Derivative:
    source: DerivativeSR
    receiver: DerivativeSR
    dpddeg: float

    @classmethod
    def from_json(cls, jsonObj):
        return Derivative(
            DerivativeSR.from_json(jsonObj['source']),
            DerivativeSR.from_json(jsonObj['receiver']),
            jsonObj['dpddeg']
            )
