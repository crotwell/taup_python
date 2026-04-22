from dataclasses import dataclass

@dataclass
class DistCalcType:
    type: str
    radius: float
    equitorialradius: float|None = None
    invflattening: float|None = None

    @classmethod
    def from_json(cls, jsonObj):
        lld = DistCalcType(
            jsonObj['type'],
            jsonObj['radius']
            )
        if 'equitorialradius' in jsonObj:
            lld.equitorialradius = jsonObj['equitorialradius']
        if 'invflattening' in jsonObj:
            lld.invflattening = jsonObj['invflattening']
        return lld
