from dataclasses import dataclass, field


@dataclass
class TimeDist:
    distdeg: float
    depth: float
    time: float
    lat: float | None
    lon: float | None

    @classmethod
    def from_json(cls, jsonObj):
        return TimeDist(*jsonObj)

    def __str__(self):
        latlon = ""
        if self.lat is not None and self.lon is not None:
            latlon = f" ({self.lat}/{self.lon})"
        return f"distdeg={self.distdeg} depth={self.depth} time={self.time}{latlon}"
