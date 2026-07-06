#!/usr/bin/env python

import taup
import json
import os

modelfilename = "mymodel.json"

with taup.TauPServer() as taupserver:

    try:
        with open(modelfilename, "r") as invmod:
            model = invmod.read()
        params = taup.TimeQuery()
        params.velocitymodeltext(model)
        params.phase(["P", "S"])
        params.degree(35)
        timeResult = params.calc(taupserver)
        if len(timeResult.arrivals) == 0:
            print(f"No arrivals...")
        else:
            print("Phase  Depth   Dist   Time")
            for a in timeResult.arrivals:
                print(f"{a.phase}      {a.sourcedepth}     {a.distdeg}   {a.time}")
    except json.JSONDecodeError as e:
        print("Trouble decoding JSON:")
        print(e)
        raise e
    except:
        print(f"Could't find {modelfilename}, downloading iasp91 and saving as mymodel.json")
        print("Edit mymodel.json and then rerun...")
        velmodParams = taup.VelmergeQuery()
        velmodParams.model("iasp91")
        print(f"cmd: {velmodParams.asCommandLine(taupserver)}")
        modelJson = velmodParams.calcJson(taupserver)
        with open(modelfilename, "w") as outmod:
            json.dump(modelJson, outmod, indent=2)
