from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .Arrival import Arrival


@dataclass
class RelativeArrival:
    difference: float
    arrival: Any  #Arrival
