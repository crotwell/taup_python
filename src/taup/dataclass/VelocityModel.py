from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .VelocityLayer import VelocityLayer, VelocityLayerParams
from .NamedDiscon import NamedDiscon

@dataclass
class VelocityModel:
    modelname: str
    modelradius: float
    minradius: float
    maxradius: float
    spherical: bool
    nameddisons: list = field(default_factory=list)
    layers: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = VelocityModel(
            jsonObj['modelname'],
            jsonObj['modelradius'],
            jsonObj['minradius'],
            jsonObj['maxradius'],
            jsonObj['spherical'])
        
        for arr in jsonObj['layers']:
            res.layers.append(VelocityLayer.from_json(arr))
        for arr in jsonObj['nameddisons']:
            res.nameddisons.append(NamedDiscon.from_json(arr))
        return res