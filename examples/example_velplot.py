#!/usr/bin/env python

import taup

with taup.TauPServer() as taupserver:

    params = taup.VelplotQuery()
    params.model(['ak135', 'prem'])
    # calculate results, parsed as JSON and returned as dataclass objects
    velResult = params.calc(taupserver)
    print(",".join(velResult.modelnames))
    for c in velResult.curves:
        print(f"curve {c.label} is {c.description}")
