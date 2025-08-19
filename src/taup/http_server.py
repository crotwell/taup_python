
from threading  import Thread, Event
from pathlib import Path
import json
import shutil
import subprocess
import time
import random
import requests
import sys

from .taupversion import TAUP_VERSION

VERBOSE=False

"""
This starts the 'taup web' process within the script, avoiding a two step
process to get the results. Many queries can be sent to the server,
saving significant spin up/shutdown time.
"""
class TauPServer:
    def __init__(self, taup_path=None, verbose=VERBOSE):
        self.verbose = verbose
        self.port = f"{random.randrange(40000, 60000)}"
        if taup_path is None:
            self.taup_path=shutil.which("taup")
        else:
            self.taup_path=taup_path
        if self.taup_path is None:
            raise Exception(f"Cannot find executable for taup, not on PATH?")
        self.taup_path = Path(self.taup_path).expanduser().resolve()
        if not self.taup_path.exists():
            raise Exception(f"{self.taup_path} doesn't exist, TauP Toolkit not on installed?")
        if self.verbose:
            print(f"TauP: {self.taup_path}", file=sys.stderr)
        self._taup = None
        self._stop_event = None

    def __enter__(self):
        self._cmd = [str(self.taup_path), "web", "-p", self.port]
        self._taup = subprocess.Popen(self._cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, close_fds=True)
        if self.verbose: print(f"starting... {' '.join(self._cmd)}", file=sys.stderr)
        time.sleep(1)
        # read a line, makes sure service has had time to start
        # we should see a line with the url like
        # http://localhost:7409
        # once the server has had a chance to be fully started up
        startupOk = False
        startLines = []
        for i in range(4):
            line = self._taup.stdout.readline().decode("utf-8")
            line = line.strip()
            startLines.append(line)
            if line.startswith("http"):
                startupOk = True
        if not startupOk:
            raise Exception("Unable to startup taup web:"+("\n".join(startLines)))

        # thread just to pull taup stdout and print it to our stderr output
        def copyStdOut(out, stop_event):
            try:
                while not stop_event.is_set():
                    line = out.readline().decode("utf-8").strip()
                    if self.verbose and len(line) > 0:
                        print(f"TauP: {line}", file=sys.stderr)
            except Exception as err:
                print('exception, quitting copy to stderr', file=sys.stderr)
                print(err, file=sys.stderr)
                return
        self._stop_event=Event()
        t = Thread(target=copyStdOut, daemon=True, args=(self._taup.stdout, self._stop_event))
        t.start()
        self.checkVersion()
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
            if self.verbose: print("TauP shutdown...", file=sys.stderr)
        if self._stop_event is not None:
            self._stop_event.set()
            self._stop_event = None


    def checkVersion(self):
        """
        Compare version these python bindings were created for with the version of the server.
        Prints a message to stderr if not the same.
        Returns the server version.
        """
        serverVersion = self.queryJson({}, "version")
        serverVersion = serverVersion['version']
        sVerMajor, sVerMinor, sVerMicro = serverVersion.split('.', maxsplit=2)
        sVerSnap = None
        if '-' in sVerMicro:
            sVerMicro, _dash, sVerSnap = sVerMicro.partition('-')

        myVerSnap = None
        myVerMajor, myVerMinor, myVerMicro = TAUP_VERSION.split('.', maxsplit=2)
        if '-' in myVerMicro:
            myVerMicro, _dash, myVerSnap = myVerMicro.partition('-')

        if sVerMajor != myVerMajor:
            message = f"Major version mismatch! {sVerMajor} != {myVerMajor}"
            self.printVersionWarnMsg(message, serverVersion, TAUP_VERSION)
        elif sVerMinor != myVerMinor:
            message = f"Minor version mismatch! {sVerMinor} != {myVerMinor}"
            self.printVersionWarnMsg(message, serverVersion, TAUP_VERSION)
        elif sVerMicro != myVerMicro:
            message = f"Micro version mismatch! {sVerMicro} != {myVerMicro}"
            self.printVersionWarnMsg(message, serverVersion, TAUP_VERSION)
        elif sVerSnap != myVerSnap:
            message = f"Snapshot Versions not compatible? {sVerSnap} != {myVerSnap}"
            self.printVersionWarnMsg(message, serverVersion, TAUP_VERSION)
        return serverVersion

    def printVersionWarnMsg(self, message, serverVersion, myVersion):
        warn = f"""
        WARNING: TauP server => Python client version mismatch!
        {message}
        This may cause errors. It is recommended that you upgrade to match.
            The TauP Toolkit (Java):
                https://taup.readthedocs.io/en/latest/
                https://doi.org/10.5281/zenodo.15426279
            TauPy (Python):
                https://pypi.org/XXXXXXXX
            Server: {serverVersion}
            Python: {TAUP_VERSION}
        """
        print(warn, file=sys.stderr)

    def retrieveTextual(self, params, tool="time", format="text"):
        if self._taup is None:
            raise Exception("TauP is None???")
        if hasattr(params, "create_params"):
            params = params.create_params()
        taup_url = f'http://localhost:{self.port}/{tool}'
        params['format'] = format
        if self.verbose:
            print(f"Query: {taup_url}", file=sys.stderr)
            print(f"Params: {json.dumps(params)}", file=sys.stderr)
        r = requests.get(taup_url, params=params, timeout=3)
        return r.text

    def retrieveJson(self, params, tool="time"):
        if self._taup is None:
            raise Exception("TauP is None???")
        if hasattr(params, "create_params"):
            params = params.create_params()
        taup_url = f'http://localhost:{self.port}/{tool}'
        if self.verbose:
            print(f"Query: {taup_url}", file=sys.stderr)
            print(f"Params: {json.dumps(params)}", file=sys.stderr)
        r = requests.get(taup_url, params=params, timeout=3)
        jsonResult = r.json()
        return jsonResult

    def queryJson(self, params, tool="time"):
        if "format" not in params:
            params["format"] = "json"
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
