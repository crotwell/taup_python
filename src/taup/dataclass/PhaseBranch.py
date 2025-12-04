from dataclasses import dataclass, field

@dataclass
class PhaseBranch:
    name: str
    updown: str
    type: str
    branch_desc: str
    then: str
    branches: list = field(default_factory=list)
    depths: list = field(default_factory=list)

    @classmethod
    def from_json(cls, jsonObj):
        res = PhaseBranch(
            jsonObj['name'],
            jsonObj['updown'],
            jsonObj['type'],
            jsonObj['branch_desc'],
            jsonObj['then']
            )
        res.branches = jsonObj['branches']
        res.depths = jsonObj['depths']
        return res
