
from threading  import Thread, Event
from pathlib import Path
import json
import shutil
import subprocess
import time
import random
import requests
import sys
import traceback

from .taupversion import TAUP_VERSION
from . import __version__

VERBOSE=False

POST="POST"
GET="GET"
DEFAULT_METHOD=POST

"""
This starts the 'taup web' process within the script, avoiding a two step
process to get the results. Many queries can be sent to the server,
saving significant spin up/shutdown time.
"""
class TauPServer:
    def __init__(self, taup_path=None, verbose=VERBOSE):
        self.method=DEFAULT_METHOD
        self.verbose = verbose
        self.port = f"{random.randrange(40000, 60000)}"
        if taup_path is None:
            self.taup_path=shutil.which("taup")
        else:
            self.taup_path=taup_path
        if self.taup_path is None:
            raise Exception(f"""\
                            Cannot find executable for taup, not on PATH?
                            Download from https://doi.org/10.5281/zenodo.10794857
                            or
                            brew tap crotwell/crotwell
                            brew install taup
                            """)
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
        for i in range(10):
            line = self._taup.stdout.readline().decode("utf-8")
            line = line.strip()
            startLines.append(line)
            if line.startswith("http") or line.startswith("TauP Web"):
                startupOk = True
            if self.verbose:
                print(line, file=sys.stderr)
            if startupOk:
                break
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
                traceback.print_exception(err, file=sys.stderr)
                return
        self._stop_event=Event()
        self._stdout_thread = Thread(target=copyStdOut, daemon=True, args=(self._taup.stdout, self._stop_event))
        self._stdout_thread.start()
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
        Returns tuple of isMatchOk, message, the server version, python version.
        """
        # do this as GET as old TauP did not allow POST
        params = {}
        params["format"] = "json"
        serverVersion = self.retrieveJson(params, "version", GET)
        serverVersion = serverVersion['version']
        sVerMajor, sVerMinor, sVerMicro = serverVersion.split('.', maxsplit=2)
        sVerSnap = None
        if '-' in sVerMicro:
            sVerMicro, _dash, sVerSnap = sVerMicro.partition('-')

        myVerSnap = None
        myVerMajor, myVerMinor, myVerMicro = TAUP_VERSION.split('.', maxsplit=2)
        if '-' in myVerMicro:
            myVerMicro, _dash, myVerSnap = myVerMicro.partition('-')

        serverIsOk = False
        message="Not OK"
        if sVerMajor != myVerMajor:
            message = f"Major version mismatch! {sVerMajor} != {myVerMajor}"
        elif sVerMinor != myVerMinor:
            message = f"Minor version mismatch! {sVerMinor} != {myVerMinor}"
        elif sVerMicro != myVerMicro:
            message = f"Micro version mismatch! {sVerMicro} != {myVerMicro}"
        elif sVerSnap != myVerSnap:
            message = f"Snapshot Versions not compatible? {sVerSnap} != {myVerSnap}"
        else:
            serverIsOk = True
            message = "OK: Server version matches Python client version."
        if not serverIsOk:
            self.printVersionWarnMsg(message, serverVersion, TAUP_VERSION)

        return serverIsOk, message, serverVersion, TAUP_VERSION

    def printVersionWarnMsg(self, message, serverVersion, myVersion):
        warn = f"""

        WARNING: TauP server <==> Python client version mismatch!

        {message}

        This may cause errors. It is recommended that you upgrade to match.
            The TauP Toolkit (Java):
                https://taup.readthedocs.io/en/latest/
                https://doi.org/10.5281/zenodo.10794857
            TauPy (Python):
                version: {__version__}
                https://pypi.org/project/taup/
            The TauP Toolkit server is {serverVersion}
            But Python was generated for {TAUP_VERSION}
        """
        print(warn, file=sys.stderr)

    def retrieveTextual(self, params, tool="time", format="text"):
        if self._taup is None:
            raise Exception("TauP is None???")
        if hasattr(params, "create_params"):
            params = params.create_params()
        taup_url = f'http://localhost:{self.port}/{tool}'
        params['format'] = format
        try:
            r = self.do_request(taup_url, params)
        except requests.ConnectionError:
            print("Connection error to taup, retrying...")
            r = self.do_request(taup_url, params)
        return r.text

    def retrieveJson(self, params, tool="time", method=None):
        if self._taup is None:
            raise Exception("TauP is None???")
        if hasattr(params, "create_params"):
            params = params.create_params()
        taup_url = f'http://localhost:{self.port}/{tool}'
        try:
            r = self.do_request(taup_url, params, method=method)
        except requests.ConnectionError:
            print("Connection error to taup, retrying...")
            r = self.do_request(taup_url, params, method=method)

        if 'content-type' in r.headers and r.headers['content-type']=='application/json':
            jsonResult = r.json()
            return jsonResult
        else:
            raise Exception(f"TauP response error: {r.text}")

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


    def do_request(self, taup_url, params, method=None):
        if method is None:
            method = self.method
        if self.verbose:
            print(f"{method} Query: {taup_url}", file=sys.stderr)
            print(f"Params: {json.dumps(params)}\n", file=sys.stderr)
        headers = {}
        if "format" in params:
            if params["format"]=="json":
                headers["Accept"] = "application/json"
            elif params["format"] in ["text", "gmt", "nd", "tvel", "locsat"]:
                headers["Accept"] = "text/plain"
            elif params["format"]=="svg":
                headers["Accept"] = "image/svg+xml"
            elif params["format"]=="csv":
                headers["Accept"] = "text/csv"
            elif params["format"]=="html":
                headers["Accept"] = "text/html"
            elif params["format"]=="sac" or params["format"]=="ms3":
                headers["Accept"] = "application/octet-stream"
        if method == GET:
            r = requests.get(taup_url, params=params, timeout=3)
        elif method == POST:
            r = requests.post(taup_url, data=json.dumps(params), timeout=3)
        else:
            raise Exception(f"Unknown method: {method}")
        r.raise_for_status()
        return r
