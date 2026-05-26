import taup

with taup.TauPServer(verbose=True) as taupserver:
    timeParams = taup.TimeQuery()
    timeParams.phase(["P", "S"])
    timeParams.mod('ak135')
    timeParams.degree(35)
    timeResult = timeParams.calc(taupserver)
    print("Phase  Depth   Dist   Time")
    for a in timeResult.arrivals:
        print(f"{a.phase}      {a.sourcedepth}     {a.distdeg}   {a.time}")
print("Done")
