from dataclasses import dataclass


@dataclass
class LatLonDepth:
    lat: float
    lon: float
    depth: float
    desc: str|None = None

    @classmethod
    def from_json(cls, jsonObj):
        lld = LatLonDepth(
            jsonObj['lat'],
            jsonObj['lon'],
            jsonObj['depth'])
        if 'desc' in jsonObj:
            lld.desc = jsonObj['desc']
        return lld
