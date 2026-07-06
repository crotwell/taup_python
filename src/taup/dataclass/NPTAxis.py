from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .SphericalCoord import SphericalCoord

@dataclass
class NPTAxis:
    n: SphericalCoord
    p: SphericalCoord
    t: SphericalCoord

    @classmethod
    def from_json(cls, jsonObj):
        res = NPTAxis(
                SphericalCoord.from_json(jsonObj['n']),
                SphericalCoord.from_json(jsonObj['n']),
                SphericalCoord.from_json(jsonObj['n']))
        return res
