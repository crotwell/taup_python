from dataclasses import dataclass
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
    def from_json(cls, jsonObj):
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


@dataclass
class VelocityLayer:
    num: int
    top: VelocityLayerParams
    bot: VelocityLayerParams


    @classmethod
    def from_json(cls, jsonObj):
        res = VelocityLayer(
            jsonObj['num'],
            VelocityLayerParams.from_json(jsonObj['top']),
            VelocityLayerParams.from_json(jsonObj['bot']))
        return res
