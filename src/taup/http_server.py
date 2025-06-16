
from threading  import Thread, Event
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
        for i in range(3):
            line = self._taup.stdout.readline().decode("utf-8")
            print(line)
            line = line.strip()
            if line.startswith("http"):
                print("startup ok")
                # set

        # thread just to pull taup stdout and print it to our output
        def copyStdOut(out, stop_event):
            try:
                while not stop_event.is_set():
                    line = out.readline().decode("utf-8")
                    print(f"TauP: {line}", file=sys.stderr)
            except Exception as err:
                print('exception, quitting copy to stdou')
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
            self._taup=None
        if self._stop_event is not None:
            self._stop_event.set()
            self._stop_event = None

    def queryJson(self, params):
        if self._taup is None:
            raise Error("TauP is None???")
        r = requests.get(f'http://localhost:{self.port}/time', params=params, timeout=3)
        jsonTimes = r.json()
        return jsonTimes
