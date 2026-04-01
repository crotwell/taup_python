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
        attenFreq = jsonObj['attenuationfreq'] if 'attenuationfreq' in jsonObj else 1
        numFreq = jsonObj['numFrequencies'] if 'numFrequencies' in jsonObj else 1
        source = Source(jsonObj['Mw'], attenFreq, numFreq)
        if "fault" in jsonObj:
            source.fault = Fault.from_json(jsonObj['fault'])
        return source
