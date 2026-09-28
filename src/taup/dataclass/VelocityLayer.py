from dataclasses import dataclass, asdict
from typing import TYPE_CHECKING


@dataclass
class VelocityLayerParams:
    depth: float
    vp: float
    vs: float
    density: float|None=None
    qp: float|None=None
    qs: float|None=None

    @classmethod
    def from_json(cls, jsonObj) -> 'VelocityLayerParams':
        res = VelocityLayerParams(
            jsonObj['depth'],
            jsonObj['vp'],
            jsonObj['vs'])
        if 'density' in jsonObj:
            res.density = jsonObj['density']
        if 'qp' in jsonObj:
            res.qp = jsonObj['qp']
        if 'qs' in jsonObj:
            res.qs = jsonObj['qs']
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)


@dataclass
class VelocityLayer:
    num: int
    top: VelocityLayerParams
    bot: VelocityLayerParams


    @classmethod
    def from_json(cls, jsonObj) -> 'VelocityLayer':
        res = VelocityLayer(
            jsonObj['num'],
            VelocityLayerParams.from_json(jsonObj['top']),
            VelocityLayerParams.from_json(jsonObj['bot']))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
