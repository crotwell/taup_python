from dataclasses import dataclass, asdict


@dataclass
class RayType:
    type: str
    ray: object

    @classmethod
    def from_json(cls, jsonObj) -> "RayType":
        return RayType(jsonObj["type"], jsonObj["ray"])

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
