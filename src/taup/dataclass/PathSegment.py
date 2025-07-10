from dataclasses import dataclass, field

@dataclass
class PathSegment:
    name: str
    wavetype: str
    segment: list[list[float]] = field(default_factory=list)
