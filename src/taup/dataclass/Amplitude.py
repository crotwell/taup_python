from dataclasses import dataclass

from .Source import Source

@dataclass
class Amplitude:
    factorpsv: float
    factorsh: float
    geospread: float
    attenuation: float
    freeFactor: float
    radiationPattern: list
    radiationTerm: float
    mgtokg: float
    refltranpsv: float
    refltransh: float
    source: Source

    @classmethod
    def from_json(cls, jsonObj):
        return Amplitude(
            jsonObj['factorpsv'],
            jsonObj['factorsh'],
            jsonObj['geospread'],
            jsonObj['attenuation'],
            jsonObj['freeFactor'],
            jsonObj['radiationPattern'],
            jsonObj['radiationTerm'],
            jsonObj['mgtokg'],
            jsonObj['refltranpsv'],
            jsonObj['refltransh'],
            Source.from_json(jsonObj['source'])
            )
