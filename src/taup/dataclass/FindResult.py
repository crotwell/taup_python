from dataclasses import dataclass, field
from typing import TYPE_CHECKING


@dataclass
class FindResult:
    model: str
    maxactions: int
    exclude: list = field(default_factory=list)
    foundphases: list = field(default_factory=list)
    sourcedepthlist: list = field(default_factory=list)
    receiverdepthlist: list = field(default_factory=list)
    phases: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = FindResult(
            jsonObj['model'],
            jsonObj['maxactions'],
            jsonObj['exclude'],
            jsonObj['foundphases'],
            jsonObj['sourcedepthlist'],
            jsonObj['receiverdepthlist'],
            jsonObj['phases'],
            )
        return res