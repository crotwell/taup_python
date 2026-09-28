from dataclasses import dataclass, asdict

@dataclass
class DistCalcType:
    type: str
    radius: float
    equitorialradius: float|None = None
    invflattening: float|None = None

    @classmethod
    def from_json(cls, jsonObj) -> 'DistCalcType':
        lld = DistCalcType(
            jsonObj['type'],
            jsonObj['radius']
            )
        if 'equitorialradius' in jsonObj:
            lld.equitorialradius = jsonObj['equitorialradius']
        if 'invflattening' in jsonObj:
            lld.invflattening = jsonObj['invflattening']
        return lld

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
