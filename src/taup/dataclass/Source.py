from dataclasses import dataclass

from .Fault import Fault

@dataclass
class Source:
    Mw: float
    attenuationfreq: float
    numFrequencies: int
    fault: Fault = None

    @classmethod
    def from_json(cls, jsonObj):
        source = Source(jsonObj['Mw'], jsonObj['attenuationfreq'], jsonObj['numFrequencies'])
        if "fault" in jsonObj:
            source.fault = Fault.from_json(jsonObj['fault'])
        return source
