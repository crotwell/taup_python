from dataclasses import dataclass, asdict


@dataclass
class LatLonDepth:
    lat: float
    lon: float
    depth: float
    desc: str | None = None

    @classmethod
    def from_json(cls, jsonObj) -> "LatLonDepth":
        lld = LatLonDepth(jsonObj["lat"], jsonObj["lon"], jsonObj["depth"])
        if "desc" in jsonObj:
            lld.desc = jsonObj["desc"]
        return lld

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
