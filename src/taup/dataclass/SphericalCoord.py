from dataclasses import dataclass
from typing import TYPE_CHECKING

@dataclass
class SphericalCoord:
    az: float
    takeoff: float

    @classmethod
    def from_json(cls, jsonObj):
        res = SphericalCoord(
                jsonObj['az'],
                jsonObj['takeoff'])
        return res

    @property
    def azimuth(self):
        return self.az
