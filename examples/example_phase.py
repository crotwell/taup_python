#!/usr/bin/env python

import taup

with taup.TauPServer() as taupserver:
    params = taup.PhaseQuery()
    params.phase(["P", "S"])
    params.sourcedepth(35)
    taupResult = params.calc(taupserver)
    if len(taupResult.descriptions) == 0:
        print(f"No descriptions...")
    else:
        print("Phase  SourceDepth   MinDist   MaxDist")
        for a in taupResult.descriptions:
            print(f"{a.name}      {a.sourcedepth}     {a.minexists.dist}   {a.maxexists.dist}")
            for seg in a.segments:
                for bs in seg.branchseq:
                    print(f"    {bs.name} {bs.updown} depth {bs.depths[0]} to {bs.depths[1]} then {bs.then}")
                print()
