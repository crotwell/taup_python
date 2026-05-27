
Manual
======

The TauP Python library allows Python scripts to easily access calculations from the TauP Toolkit. This is done
by having the Python script, internally, start up the TauP http server. Queries are then sent to this server
via http over a local socket, and the response is returned and usually parsed into Python objects that are easier
to use.

Initialization
--------------

The fundamental pattern is that the server should only be started once, and reused throughout the script. If on
the other hand, a new server is repeatedly started up and shutdown after one query, the speed benefits are
largely lost as the time cost to spin up the server will be paid for each instance created. The server implements
the Python pattern that allows it to be used via the :code:`with` statement, and so a typical script would look 
like:

.. code-block::

    import taup

    with taup.TauPServer() as taupserver:
        params = taup.TimeQuery()
        params.degree(35)
        # add more items to params for your query
        result = params.calc(taupserver)
        # do stuff with the result

If many different calculations need to be performed, it is very important that the loop be inside of the 
:code:`with` statement. So for example if we wished to loop over a list of distances to get P arrival times,
the script should look like this. Note that the :code:`for` loop is inside the :code:`with` block. The query object for the tool, 
like :code:`taup.TimeQuery`, does not have to be created inside the loop, and as it is just a simple container for
the parameters, it can be modified and reused. 
The :code:`calc()` method on the other hand must be inside as it handles
the actual communication back and forth from the server.

.. code-block::

    import taup

    my_distances = [ 10, 20, 30 ]
    with taup.TauPServer() as taupserver:
        params = taup.TimeQuery()
        params.phase("P")
        # add items to params for your query
        for dist in my_distances:
            params.degree(dist)
            result = params.calc(taupserver)
            # do stuff with the result

Query Parameters
-------------------

There are separate query objects for each tool, for example :code:`TimeQuery` for travel times, 
:code:`PierceQuery` for pierce points and :code:`PathQuery` for paths. These correspond one to one with
the command line tools in the TauP Toolkit, :code:`TimeQuery` to :code:`taup time` and :code:`PierceQuery`
to :code:`taup pierce`. The options available with the query objects also correspond one to one with the
command line arguments, and indeed are automatically generated from the command line arguments in the java
code. So for example, within the :code:`taup time` tool, you can use the :code:`--degree` option to specify
distance in degrees. Within the :code:`TimeQuery` object, there is a :code:`degree()` method that also takes
distances in degrees and will pass them on to the internal instance of :code:`taup time` in exactly the same 
manner. So the first example above should generate the same results as:

.. code-block::

    taup time --degree 35

There is one slight distinction in that the textual output of :code:`taup time` is formatted, and so it does not
show each number at full precision. To be more correct, that first example most resembles

.. code-block::

    taup time --degree 35 --json

where the resulting json is turned into a python object for easier access. We next look at these result objects.


Calculation Results
-------------------

The :code:`calc()` method on each of the :code:`Query` objects sends all the given parameters to the corresponding
tool via the server, but also appending one additional parameter, setting the returned format to be 
`JSON <http://json.org>`__ as if using the :code:`--json` command line argument. 
It then also parses the returned result and converts it into Python dataclasses. This
makes it easier to access the internal values, for example you use :code:`result.arrivals` to get the arrivals
as a list instead of the less readable :code:`result['arrivals']` that would result from directly using the JSON.
Note however, that if the raw JSON is desired, there is a :code:`calcJson()` method that parses the JSON and
returns it directly.

For other tools, like :code:`taup path`, it may be more desirable to get the results as an image. For this,
tools that support SVG output will have a :code:`calcSvg()` method in addition. This is SVG as text, and so 
is not an image exactly, but can be displayed by a SVG renderer, or perhaps just saved to a file locally.

There are similar calculation methods for the other formats supported by each individual tool, including  
text, :code:`calcText()`; 
`JSON <http://json.org>`__, :code:`calcJson()`; 
`SVG <https://www.w3.org/Graphics/SVG/About>`__, :code:`calcSvg()`; 
`GMT <https://www.generic-mapping-tools.org/>`__ scripts, :code:`calcGmt()`; 
HTML, :code:`calcHtml()` and
CSV, :code:`calcCsv()`.
Note that not every tool supports every format, so see the documentation for each tool to see what exists. 
But text and JSON are always supported for every tool.

Examples
--------

There are simple examples for every tool in the 
`examples <https://github.com/crotwell/taup_python/tree/main/examples>`__
directory of the source code distribution.

See also the API documentation for each tool to see what options are available:

* :py:class:`.BeachballQuery`
* :py:class:`.CurveQuery`
* :py:class:`.DisconQuery`
* :py:class:`.DistazQuery`
* :py:class:`.FindQuery`
* :py:class:`.PathQuery`
* :py:class:`.PhaseQuery`
* :py:class:`.PierceQuery`
* :py:class:`.RefltransQuery`
* :py:class:`.TableQuery`
* :py:class:`.TimeQuery`
* :py:class:`.VelmergeQuery`
* :py:class:`.VelplotQuery`
* :py:class:`.VersionQuery`
* :py:class:`.WavefrontQuery`