from dataclasses import dataclass, asdict


@dataclass
class DisconLayer:
    Vp: float
    Vs: float
    density: float
    slowness_p: float
    slowness_s: float

    @classmethod
    def from_json(cls, jsonObj) -> "DisconLayer":
        return DisconLayer(
            jsonObj["vp"],
            jsonObj["vs"],
            jsonObj["density"],
            jsonObj["slowness_p"],
            jsonObj["slowness_s"],
        )

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)


@dataclass
class Discontinuity:
    depth: float
    name: str | None
    preferredname: str | None
    above: DisconLayer | None
    below: DisconLayer | None

    @classmethod
    def from_json(cls, jsonObj) -> "Discontinuity":
        above = None
        if "above" in jsonObj:
            l = jsonObj["above"]
            above = DisconLayer.from_json(l)
        below = None
        if "below" in jsonObj:
            l = jsonObj["below"]
            below = DisconLayer.from_json(l)
        return Discontinuity(
            jsonObj["depth"],
            jsonObj["name"] if "name" in jsonObj else None,
            jsonObj["preferredname"] if "preferredname" in jsonObj else None,
            above,
            below,
        )

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)


@dataclass
class ModelDiscon:
    modelname: str
    discontinuities: list[Discontinuity]

    @classmethod
    def from_json(cls, jsonObj) -> "ModelDiscon":
        disconResult = []
        for d in jsonObj["discontinuities"]:
            disconResult.append(Discontinuity.from_json(d))
        return ModelDiscon(jsonObj["modelname"], disconResult)

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)


@dataclass
class DisconResult:
    models: list[ModelDiscon]

    @classmethod
    def from_json(cls, jsonObj) -> "DisconResult":
        modelResults = []
        for mr in jsonObj["models"]:
            modelResults.append(ModelDiscon.from_json(mr))
        res = DisconResult(modelResults)
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
