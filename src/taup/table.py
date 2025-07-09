class TableQuery:
  def __init__(self):
    self.toolname= "table"

    self._generic=None
    self._header=None
    self._model=None
    self._phase=[]
    self._receiverdepth=[]
    self._scatter=[]

  def calc(self, taupServer):
    """
    Sends all params to the server, returns the result parsed from JSON.
    """
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def calcHtml(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of html.
    """
    params = self.create_params()
    return taupServer.queryHtml(params, self.toolname)


  def calcCsv(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of csv.
    """
    params = self.create_params()
    return taupServer.queryCsv(params, self.toolname)


  def calcText(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of text.
    """
    params = self.create_params()
    return taupServer.queryText(params, self.toolname)


  def calcLocsat(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of locsat.
    """
    params = self.create_params()
    return taupServer.queryLocsat(params, self.toolname)


  def get_text(self):
    """
    returns current value of generic as a Boolean
    """
    return self._generic

  def text(self, val):
    """
    Sets the generic parameter, of type Boolean
    
    outputs as Text

    Known as --text in command line.
    Also known as --generic in command line.

    :param val: value to set generic to
    """
    self._generic = val
    return self

  def get_generic(self):
    """
    returns current value of generic as a Boolean
    """
    return self._generic

  def generic(self, val):
    """
    Sets the generic parameter, of type Boolean
    
    outputs as Text

    Known as --generic in command line.

    :param val: value to set generic to
    """
    self._generic = val
    return self

  def get_header(self):
    """
    returns current value of header as a String
    """
    return self._header

  def header(self, val):
    """
    Sets the header parameter, of type String
    
    reads depth and distance spacing data from a LOCSAT style file.

    Known as --header in command line.

    :param val: value to set header to
    """
    self._header = val
    return self

  def get_mod(self):
    """
    returns current value of model as a String
    """
    return self._model

  def mod(self, val):
    """
    Sets the model parameter, of type String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.

    Known as --mod in command line.
    Also known as --model in command line.

    :param val: value to set model to
    """
    self._model = val
    return self

  def get_model(self):
    """
    returns current value of model as a String
    """
    return self._model

  def model(self, val):
    """
    Sets the model parameter, of type String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.

    Known as --model in command line.

    :param val: value to set model to
    """
    self._model = val
    return self

  def get_p(self):
    """
    returns current value of phase as a List
    """
    return self._phase

  def p(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.p( value )
    and 
    .xp( [ value ] )
    are equivalent. 
    
    seismic phase names

    Known as -p in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self


  def andP(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.p( value )
    and 
    .xp( [ value ] )
    are equivalent. 
    
    seismic phase names

    Known as -p in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_phase(self):
    """
    returns current value of phase as a List
    """
    return self._phase

  def phase(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phase( value )
    and 
    .xphase( [ value ] )
    are equivalent. 
    
    seismic phase names

    Known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self


  def andPhase(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phase( value )
    and 
    .xphase( [ value ] )
    are equivalent. 
    
    seismic phase names

    Known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_ph(self):
    """
    returns current value of phase as a List
    """
    return self._phase

  def ph(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.ph( value )
    and 
    .xph( [ value ] )
    are equivalent. 
    
    seismic phase names

    Known as --ph in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self


  def andPh(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.ph( value )
    and 
    .xph( [ value ] )
    are equivalent. 
    
    seismic phase names

    Known as --ph in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_stadepth(self):
    """
    returns current value of receiverdepth as a List
    """
    return self._receiverdepth

  def stadepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.stadepth( value )
    and 
    .xstadepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface

    Known as --stadepth in command line.
    Also known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self


  def andStadepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.stadepth( value )
    and 
    .xstadepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface

    Known as --stadepth in command line.
    Also known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    self._receiverdepth.append(val)
    return self

  def get_receiverdepth(self):
    """
    returns current value of receiverdepth as a List
    """
    return self._receiverdepth

  def receiverdepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.receiverdepth( value )
    and 
    .xreceiverdepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface

    Known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self


  def andReceiverdepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.receiverdepth( value )
    and 
    .xreceiverdepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface

    Known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    self._receiverdepth.append(val)
    return self

  def get_scat(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scat(self, depth, degree):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.

    Known as --scat in command line.
    Also known as --scatter in command line.

    :param val: value to set scatter to
    """
    self._scatter = [depth, degree]
    return self

  def get_scatter(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scatter(self, depth, degree):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.

    Known as --scatter in command line.

    :param val: value to set scatter to
    """
    self._scatter = [depth, degree]
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._generic is not None:
      params["generic"] = self._generic
    if self._header is not None:
      params["header"] = self._header
    if self._model is not None:
      params["model"] = self._model
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    return params

