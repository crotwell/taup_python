from dataclasses import dataclass

from .LatLonDepth import LatLonDepth
from .DistCalcType import DistCalcType

@dataclass
class Daz:
    deg: float
    az: float
    baz: float
    source: LatLonDepth|None = None
    receiver: LatLonDepth|None = None
    km: float|None = None
    disttype: DistCalcType|None = None

    @classmethod
    def from_json(cls, jsonObj):
        daz = Daz(jsonObj['deg'],
                      jsonObj['az'],jsonObj['baz'],
                      [jsonObj['source']['lat'], jsonObj['source']['lon']],
                      [jsonObj['receiver']['lat'], jsonObj['source']['lon']])
        if 'source' in jsonObj:
            daz.source = LatLonDepth.from_json(jsonObj['source'])
        if 'receiver' in jsonObj:
            daz.receiver = LatLonDepth.from_json(jsonObj['receiver'])
        if "km" in jsonObj:
            daz.km = jsonObj['km']
        if "disttype" in jsonObj:
            daz.disttype = DistCalcType.from_json(jsonObj['disttype'])
        return daz
