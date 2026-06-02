#!/usr/bin/env python

import taup

with taup.TauPServer() as taupserver:
    params = taup.TimeQuery()
    params.phase(["P", "S"])
    params.degree(35)
    cmdLine = params.asCommandLine(taupserver)
    print(cmdLine)
