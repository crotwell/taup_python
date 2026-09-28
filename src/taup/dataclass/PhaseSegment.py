from dataclasses import dataclass, field, asdict

from .PhaseBranch import PhaseBranch

@dataclass
class PhaseSegment:
    maxrayparam: float
    minrayparam: float
    branchseq: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj) -> 'PhaseSegment':
        res = PhaseSegment(
            jsonObj['maxrayparam'],
            jsonObj['minrayparam']
            )
        for bs in jsonObj['branchseq']:
            res.branchseq.append(PhaseBranch.from_json(bs))
        return res

    @property
    def __dict__(self):
        """
        as a python dictionary
        """
        return asdict(self)
