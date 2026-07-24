from dataclasses import dataclass

@dataclass
class DisconLayer:
    Vp: float
    Vs: float
    density: float
    slowness_p: float
    slowness_s: float

@dataclass
class Discontinuity:
    depth: float
    name: str | None
    preferredname: str | None
    above: DisconLayer | None
    below: DisconLayer | None

    @classmethod
    def from_json(cls, jsonObj):
        above = None
        if "above" in jsonObj:
            l = jsonObj["above"]
            above = DisconLayer(l["vp"], l["vs"],
                                l["density"],
                                l["slowness_p"], l["slowness_s"])
        below = None
        if "below" in jsonObj:
            l = jsonObj["below"]
            below = DisconLayer(l["vp"], l["vs"],
                                l["density"],
                                l["slowness_p"], l["slowness_s"])
        return Discontinuity(
            jsonObj["depth"],
            jsonObj["name"] if "name" in jsonObj else None,
            jsonObj["preferredname"] if "preferredname" in jsonObj else None,
            above,
            below
        )

@dataclass
class ModelDiscon:
    modelname: str
    discontinuities: list[Discontinuity]

    @classmethod
    def from_json(cls, jsonObj):
        disconResult = []
        for d in jsonObj["discontinuities"]:
            disconResult.append(Discontinuity.from_json(d))
        return ModelDiscon(jsonObj["modelname"], disconResult)

@dataclass
class DisconResult:
    models: list[ModelDiscon]

    @classmethod
    def from_json(cls, jsonObj):
        modelResults = []
        for mr in jsonObj["models"]:
            modelResults.append(ModelDiscon.from_json(mr))
        res = DisconResult(
            modelResults)
        return res
