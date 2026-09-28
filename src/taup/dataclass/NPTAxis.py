from dataclasses import dataclass, field, asdict
from typing import TYPE_CHECKING

from .SphericalCoord import SphericalCoord

@dataclass
class NPTAxis:
    n: SphericalCoord
    p: SphericalCoord
    t: SphericalCoord

    @classmethod
    def from_json(cls, jsonObj) -> 'NPTAxis':
        res = NPTAxis(
                SphericalCoord.from_json(jsonObj['n']),
                SphericalCoord.from_json(jsonObj['p']),
                SphericalCoord.from_json(jsonObj['t']))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
