from dataclasses import dataclass

@dataclass
class RayType:
    type: str
    ray: object

    @classmethod
    def from_json(cls, jsonObj):
        return RayType(jsonObj['type'],jsonObj['ray'])
