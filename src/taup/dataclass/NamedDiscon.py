from dataclasses import dataclass, asdict


@dataclass
class NamedDiscon:
    name: str
    depth: float
    preferredname: str = ""

    @classmethod
    def from_json(cls, jsonObj) -> "NamedDiscon":
        res = NamedDiscon(jsonObj["name"], jsonObj["depth"])
        if "preferredname" in jsonObj:
            res.preferredname = jsonObj["preferredname"]
        else:
            res.preferredname = res.name
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
