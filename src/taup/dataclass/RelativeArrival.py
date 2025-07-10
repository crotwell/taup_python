from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .Arrival import Arrival


@dataclass
class RelativeArrival:
    difference: float
    arrival: Any  #Arrival

    @classmethod
    def from_json(cls, jsonObj):
        # this seems dumb, but circular references...
        from .Arrival import Arrival
        return RelativeArrival(
            jsonObj['difference'],
            Arrival.from_json(jsonObj['arrival']))
