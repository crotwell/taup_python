from dataclasses import dataclass, asdict
from typing import TYPE_CHECKING

@dataclass
class SphericalCoord:
    az: float
    takeoff: float

    @classmethod
    def from_json(cls, jsonObj) -> 'SphericalCoord':
        res = SphericalCoord(
                jsonObj['az'],
                jsonObj['takeoff'])
        return res

    @property
    def azimuth(self):
        return self.az

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
