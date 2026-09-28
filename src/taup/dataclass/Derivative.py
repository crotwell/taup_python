from dataclasses import dataclass, asdict
from .DerivativeSR import DerivativeSR


@dataclass
class Derivative:
    source: DerivativeSR
    receiver: DerivativeSR
    dpddeg: float

    @classmethod
    def from_json(cls, jsonObj) -> "Derivative":
        return Derivative(
            DerivativeSR.from_json(jsonObj["source"]),
            DerivativeSR.from_json(jsonObj["receiver"]),
            jsonObj["dpddeg"],
        )

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
