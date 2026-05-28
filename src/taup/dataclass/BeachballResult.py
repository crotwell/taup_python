from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .Arrival import Arrival
from .Source import Source

@dataclass
class BeachballResult:

    source: Source
    model: str
    sourcedepthlist: list
    receiverdepthlist: list
    phases: list
    arrivals: list = field(default_factory=list)
    radiationPattern: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = BeachballResult(
            jsonObj['source'],
            jsonObj['model'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases']
            )
        for arr in jsonObj['arrivals']:
            res.arrivals.append(Arrival.from_json(arr))

        for rp in jsonObj['radiationPattern']:
            res.radiationPattern.append(rp) # fix this to a dataclass?
        return res
