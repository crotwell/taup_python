from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from .PathSegment import PathSegment
from .Amplitude import Amplitude
from .Scatter import Scatter

if TYPE_CHECKING:
    from .RelativeArrival import RelativeArrival

@dataclass
class Arrival:
    sourcedepth: float
    receiverdepth: float
    distdeg: float
    phase: str
    time: float
    rayparam: float
    takeoff: float
    incident: float
    puristdist: float
    puristname: str
    desc: str| None = None
    amp: Amplitude| None = None
    scatter: Scatter| None = None
    relative: Any  = None # RelativeArrival
    pierce: list[list[float]] = field(default_factory=list)
    pathSegments: list[PathSegment] = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        arr = Arrival(
            jsonObj['sourcedepth'],
            jsonObj['receiverdepth'],
            jsonObj['distdeg'],
            jsonObj['phase'],
            jsonObj['time'],
            jsonObj['rayparam'],
            jsonObj['takeoff'],
            jsonObj['incident'],
            jsonObj['puristdist'],
            jsonObj['puristname']
            )
        if 'desc' in jsonObj:
            arr.desc = jsonObj['desc']
        if 'amp' in jsonObj:
            arr.amp = jsonObj['amp']
        if 'scatter' in jsonObj:
            arr.scatter = jsonObj['scatter']
        if 'relative' in jsonObj:
            arr.relative = jsonObj['relative']
        if 'pierce' in jsonObj:
            arr.pierce = jsonObj['pierce']
        if 'pathSegments' in jsonObj:
            arr.pathSegments = jsonObj['pathSegments']
        return arr
