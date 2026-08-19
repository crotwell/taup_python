from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .Arrival import Arrival
from .NPTAxis import NPTAxis
from .Beachball import Beachball

@dataclass
class BeachballResult:

    model: str
    sourcedepthlist: list
    receiverdepthlist: list
    phases: list
    arrivals: list = field(default_factory=list)
    beachballs: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = BeachballResult(
            jsonObj['model'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases'],
            )
        for arr in jsonObj['arrivals']:
            res.arrivals.append(Arrival.from_json(arr))

        for bb in jsonObj['beachballs']:
            res.beachballs.append(Beachball.from_json(bb)) # fix this to a dataclass?
        return res
