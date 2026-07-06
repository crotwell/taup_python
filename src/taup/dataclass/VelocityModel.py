from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .VelocityLayer import VelocityLayer, VelocityLayerParams

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

        for nd in jsonObj['nameddisons']:
            res.nameddisons.append(NamedDiscon.from_json(nd))
        for layer in jsonObj['layers']:
            res.layers.append(VelocityLayer.from_json(layer))
        return res


@dataclass
class NamedDiscon:
    name: str
    depth: float
    preferredname: str=""

    @classmethod
    def from_json(cls, jsonObj):
        res = NamedDiscon(
            jsonObj['name'],
            jsonObj['depth'])
        if 'preferredname' in jsonObj:
            res.preferredname = jsonObj['preferredname']
        else:
            res.preferredname = res.name
        return res
