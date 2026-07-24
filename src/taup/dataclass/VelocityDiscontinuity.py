from dataclasses import dataclass
from typing import TYPE_CHECKING


@dataclass
class VelocityParams:
    vp: float
    vs: float
    density: float

    @classmethod
    def from_json(cls, jsonObj):
        res = VelocityParams(
            jsonObj['vp'],
            jsonObj['vs'],
            jsonObj['density'])
        return res


@dataclass
class VelocityDiscontinuity:
    incident: VelocityParams
    transmitted: VelocityParams

    @classmethod
    def from_json(cls, jsonObj):
        res = VelocityDiscontinuity(
            VelocityParams.from_json(jsonObj['incident']),
            VelocityParams.from_json(jsonObj['transmitted']))
        return res
