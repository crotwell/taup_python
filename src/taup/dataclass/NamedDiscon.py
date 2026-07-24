from dataclasses import dataclass

@dataclass
class NamedDiscon:
    name: str
    depth: float
    preferredname: str=""

    @classmethod
    def from_json(cls, jsonObj):
        res = NamedDiscon(
            jsonObj['name'],
            jsonObj['depth'])
        if 'preferredname' in jsonObj:
            res.preferredname = jsonObj['preferredname']
        else:
            res.preferredname = res.name
        return res