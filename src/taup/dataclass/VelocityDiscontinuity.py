from dataclasses import dataclass, asdict
from typing import TYPE_CHECKING


@dataclass
class VelocityParams:
    vp: float
    vs: float
    density: float

    @classmethod
    def from_json(cls, jsonObj) -> 'VelocityParams':
        res = VelocityParams(
            jsonObj['vp'],
            jsonObj['vs'],
            jsonObj['density'])
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)


@dataclass
class VelocityDiscontinuity:
    incident: VelocityParams
    transmitted: VelocityParams

    @classmethod
    def from_json(cls, jsonObj) -> 'VelocityDiscontinuity':
        res = VelocityDiscontinuity(
            VelocityParams.from_json(jsonObj['incident']),
            VelocityParams.from_json(jsonObj['transmitted']))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
