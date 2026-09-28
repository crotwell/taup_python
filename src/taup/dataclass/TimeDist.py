from dataclasses import dataclass, field, asdict


@dataclass
class TimeDist:
    distdeg: float
    depth: float
    time: float
    lat: float | None = None
    lon: float | None = None

    @classmethod
    def from_json(cls, jsonObj) -> 'TimeDist':
        return TimeDist(*jsonObj)

    def __str__(self):
        latlon = ""
        if self.lat is not None and self.lon is not None:
            latlon = f" ({self.lat}/{self.lon})"
        return f"distdeg={self.distdeg} depth={self.depth} time={self.time}{latlon}"

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
