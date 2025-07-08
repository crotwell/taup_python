# taup_python

Access to the TauP Toolkit from Python via an HTTP server.

The problem is that lots of seismologists like writing Python scripts, but
calling a Java library from Python seems somewhere
between hard and impossible. But interaction doesn't require direct
interoperation. The
basic idea of this solution (or bandaid)
is that this python library will spin up an instance of `taup web`,
and then use that to answer many queries, avoiding the startup time of Java.

You will also need to have an instance of the
[TauP Toolkit](https://taup.readthedocs.io/en/latest/)
installed.

The Python classes representing each tool's query parameters are based off
off the command line arguments of the same name. For example, this Python
code:

```
with taup.TauPServer() as timeserver:
    timeParams = taup.TimeQuery()
    timeParams.phase(["P", "S"])
    timeParams.model('ak135')
    timeParams.degree(35)
    results = timeParams.calc(timeserver)
```

roughly corresponds to this command line:
```
bin/taup time --ph P,S --mod ak135 --deg 35 --json
```

Note that if you have many calculations in a loop, you want to have the loop
on the inside of the `with taup.TauPServer() as timeserver:` line so that
the server is only started up once.

See `example_times.py` and `example_text.py` for a couple of more detailed examples.
