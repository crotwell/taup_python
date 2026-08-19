from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .Arrival import Arrival
from .NPTAxis import NPTAxis
from .Fault import Fault

@dataclass
class Beachball:

    beachballtype: str
    hemisphere: str
    fault: Fault
    nptAxis: NPTAxis
    arrivals: list = field(default_factory=list)
    radiationPattern: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = Beachball(
            jsonObj['beachballtype'],
            jsonObj['hemisphere'],
            Fault.from_json(jsonObj['fault']),
            NPTAxis.from_json(jsonObj['nptAxis'])
            )
        for arr in jsonObj['arrivals']:
            res.arrivals.append(Arrival.from_json(arr))

        for rp in jsonObj['radiationPattern']:
            res.radiationPattern.append(rp) # fix this to a dataclass?
        return res
