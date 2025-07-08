
from threading  import Thread, Event
from pathlib import Path
import shutil
import subprocess
import time
import random
import requests
import sys

"""
Slightly more advanced python script. This starts the 'taup web' process
within the script, avoiding a two step process to get the results. Many
queries can be sent to the server, saving significant spin up/shutdown time.
"""
class TauPServer:
    def __init__(self, taup_path=None):
        self.port = f"{random.randrange(40000, 60000)}"
        if taup_path is None:
            self.taup_path=shutil.which("taup")
        else:
            self.taup_path=taup_path
        if self.taup_path is None:
            raise Exception(f"Cannot find executable for taup, not on PATH?")
        if not Path(self.taup_path).exists():
            raise Exception(f"{self.taup_path} doesn't exist, TauP Toolkit not on installed?")
        self._taup = None
        self._stop_event = None

    def __enter__(self):
        self._cmd = [self.taup_path, "web", "-p", self.port]
        self._taup = subprocess.Popen(self._cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, close_fds=True)
        print(f"starting... {' '.join(self._cmd)}")
        time.sleep(1)
        # read a line, makes sure service has had time to start
        # we should see a line with the url like
        # http://localhost:7409
        # once the server has had a chance to be fully started up
        startupOk = False
        startLines = []
        for i in range(4):
            line = self._taup.stdout.readline().decode("utf-8")
            #print(line)
            line = line.strip()
            startLines.append(line)
            if line.startswith("http"):
                startupOk = True
        if not startupOk:
            raise Exception("Unable to startup taup web:"+("\n".join(startLines)))

        # thread just to pull taup stdout and print it to our output
        def copyStdOut(out, stop_event):
            try:
                while not stop_event.is_set():
                    line = out.readline().decode("utf-8").strip()
                    if len(line) > 0:
                        print(f"TauP: {line}", file=sys.stderr)
            except Exception as err:
                print('exception, quitting copy to stderr')
                print(err)
                return
        self._stop_event=Event()
        t = Thread(target=copyStdOut, daemon=True, args=(self._taup.stdout, self._stop_event))
        t.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.shutdown()

    def shutdown(self):
        # close down the web server
        if self._taup is not None:
            self._taup.terminate()
            try:
                self._taup.wait(3)
            except:
                self._taup.kill()
            self._taup=None
        if self._stop_event is not None:
            self._stop_event.set()
            self._stop_event = None

    def retrieveTextual(self, params, tool="time", format="text"):
        if self._taup is None:
            raise Exception("TauP is None???")
        if hasattr(params, "create_params"):
            params = params.create_params()
        taup_url = f'http://localhost:{self.port}/{tool}'
        params['format'] = format
        print("TEXT")
        print(f"Query: {taup_url}")
        print(f"Params: {params}")
        r = requests.get(taup_url, params=params, timeout=3)
        return r.text

    def retrieveJson(self, params, tool="time"):
        if self._taup is None:
            raise Exception("TauP is None???")
        if hasattr(params, "create_params"):
            params = params.create_params()
        taup_url = f'http://localhost:{self.port}/{tool}'
        print(f"Query: {taup_url}")
        print(f"Params: {params}")
        r = requests.get(taup_url, params=params, timeout=3)
        jsonTimes = r.json()
        return jsonTimes

    def queryJson(self, params, tool="time"):
        return self.retrieveJson(params, tool=tool)

    def queryText(self, params, tool="time"):
        return self.retrieveTextual(params, tool=tool, format="text")

    def querySvg(self, params, tool="time"):
        return self.retrieveTextual(params, tool=tool, format="svg")

    def queryGmt(self, params, tool="time"):
        return self.retrieveTextual(params, tool=tool, format="gmt")

    def queryHtml(self, params, tool="time"):
        return self.retrieveTextual(params, tool=tool, format="html")

    def queryCsv(self, params, tool="time"):
        return self.retrieveTextual(params, tool=tool, format="csv")

    def queryLocsat(self, params, tool="time"):
        return self.retrieveTextual(params, tool=tool, format="locsat")
