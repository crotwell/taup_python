from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .PathSegment import PathSegment
from .Amplitude import Amplitude
from .LatLonDepth import LatLonDepth
from .RayType import RayType
from .Scatter import Scatter
from .TimeDist import TimeDist

from .RelativeArrival import RelativeArrival
from .Derivative import Derivative

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
    az: float|None = None
    baz: float|None = None
    desc: str| None = None
    sourceloc: LatLonDepth| None = None
    receiverloc: LatLonDepth| None = None
    amp: Amplitude| None = None
    scatter: Scatter| None = None
    relative: RelativeArrival|None  = None # RelativeArrival
    derivative: Derivative = None
    pierce: list[TimeDist] = field(default_factory=list)
    pathlength: float|None = None
    path: list[PathSegment] = field(default_factory=list)
    raytype: RayType|None = None

    def mergePath(self):
        mergedpath = []
        for ps in self.path:
            mergedpath = mergedpath + ps.segment
        return mergedpath

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
        if 'raytype' in jsonObj:
            arr.raytype = jsonObj['raytype']
        if 'sourceloc' in jsonObj:
            arr.sourceloc = LatLonDepth.from_json(jsonObj['sourceloc'])
        if 'receiverloc' in jsonObj:
            arr.receiverloc = LatLonDepth.from_json(jsonObj['receiverloc'])
        if 'amp' in jsonObj:
            arr.amp = Amplitude.from_json(jsonObj['amp'])
        if 'scatter' in jsonObj:
            arr.scatter = jsonObj['scatter']
        if 'relative' in jsonObj:
            arr.relative = RelativeArrival.from_json(jsonObj['relative'])
        if 'derivative' in jsonObj:
            arr.derivative = Derivative.from_json(jsonObj['derivative'])
        if 'pierce' in jsonObj:
            for p in jsonObj['pierce']:
                arr.pierce.append(TimeDist.from_json(p))
        if 'path' in jsonObj:
            arr.pathlength = jsonObj['pathlength']
            for p in jsonObj['path']:
                arr.path.append(PathSegment.from_json(p))
        return arr

    @property
    def azimuth(self):
        return self.az

    @property
    def backazimuth(self):
        return self.baz

    def __str__(self):
        return f"{self.distdeg} {self.sourcedepth} {self.phase} {self.time} {self.rayparam} {self.takeoff} {self.incident} {self.puristdist} {self.puristname}"
