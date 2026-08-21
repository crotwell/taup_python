.. taup documentation master file, created by
   sphinx-quickstart on Wed Jun 18 22:47:28 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TauP Python Interaction
=======================


Access `The TauP Toolkit <https://doi.org/10.5281/zenodo.10794857>`__ from Python.


The latest source is at GitHub,
`https://github.com/crotwell/taup_python <https://github.com/crotwell/taup_python>`__
.

Install the latest release of the TauP Toolkit, for example using  `homebrew <https://brew.sh/>`_::

  brew tap crotwell/crotwell
  brew trust --formula crotwell/crotwell/taup
  brew install taup

Then install the Python package using `pip`

.. code-block::

  pip install taup

and then start coding.

.. code-block:: python

   import taup

   with taup.TauPServer() as taupserver:
      params = taup.TimeQuery()
      params.phase(["P", "S"])
      params.degree(35)
      taupResult = params.calc(taupserver)
      if len(taupResult.arrivals) == 0:
         print(f"No arrivals...")
      else:
         print("Phase  Depth   Dist   Time")
         for a in taupResult.arrivals:
               print(f"{a.phase}      {a.sourcedepth}     {a.distdeg}   {a.time}")

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   README <readme_link>
   Manual <manual>
   apidocs/index
   Source <https://github.com/crotwell/taup_python>
   PyPI <https://pypi.org/project/taup/>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
