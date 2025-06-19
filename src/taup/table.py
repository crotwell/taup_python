class TableQuery:
  def __init__(self):
    self.toolname= "table"

    self._generic=None
    self._locsat=None
    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._phase=[]
    self._phasefile=[]
    self._header=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_text(self):
    """
    returns current value of generic as a Boolean
    """
    return self._generic

  def text(self, val):
    """
    Sets the generic parameter, of type Boolean    
    outputs as Text
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

    :param val: value to set generic to
    """
    self._generic = val
    return self

  def get_locsat(self):
    """
    returns current value of locsat as a Boolean
    """
    return self._locsat

  def locsat(self, val):
    """
    Sets the locsat parameter, of type Boolean    
    outputs as Locsat

    :param val: value to set locsat to
    """
    self._locsat = val
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

    :param val: value to set model to
    """
    self._model = val
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
    Also known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
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

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self

  def get_scat(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scat(self, val):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scatter in command line.

    :param val: value to set scatter to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"scat() requires a list, not {val}")
    self._scatter = val
    return self

  def get_scatter(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scatter(self, val):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.

    :param val: value to set scatter to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"scatter() requires a list, not {val}")
    self._scatter = val
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
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
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

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
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
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self

  def get_phasefile(self):
    """
    returns current value of phasefile as a List
    """
    return self._phasefile

  def phasefile(self, val):
    """
    Sets the phasefile parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phasefile( value )
    and 
    .xphasefile( [ value ] )
    are equivalent. 
    
    read list of phase names from file

    :param val: value to set phasefile to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phasefile = val
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

    :param val: value to set header to
    """
    self._header = val
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
    if self._locsat is not None:
      params["locsat"] = self._locsat
    if self._model is not None:
      params["model"] = self._model
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    if self._header is not None:
      params["header"] = self._header
    return params

