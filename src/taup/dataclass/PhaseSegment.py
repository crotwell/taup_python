from dataclasses import dataclass, field

from .PhaseBranch import PhaseBranch

@dataclass
class PhaseSegment:
    maxrayparam: float
    minrayparam: float
    branchseq: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = PhaseSegment(
            jsonObj['maxrayparam'],
            jsonObj['minrayparam']
            )
        for bs in jsonObj['branchseq']:
            res.branchseq.append(PhaseBranch.from_json(bs))
        return res
