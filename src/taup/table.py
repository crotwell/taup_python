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
    return self._generic

  def text(self, val):
    """
    Boolean
    
    outputs as Text
    Also known as --generic in command line.
    """
    self._generic = val
    return self

  def get_generic(self):
    return self._generic

  def generic(self, val):
    """
    Boolean
    
    outputs as Text
    """
    self._generic = val
    return self

  def get_locsat(self):
    return self._locsat

  def locsat(self, val):
    """
    Boolean
    
    outputs as Locsat
    """
    self._locsat = val
    return self

  def get_mod(self):
    return self._model

  def mod(self, val):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    Also known as --model in command line.
    """
    self._model = val
    return self

  def get_model(self):
    return self._model

  def model(self, val):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    """
    self._model = val
    return self

  def get_stadepth(self):
    return self._receiverdepth

  def stadepth(self, val):
    """
    List of Double

    
    the receiver depth in km for stations not at the surface
    Also known as --receiverdepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{stadepth} must be a list, not {val}")
    self._receiverdepth = val
    return self

  def get_receiverdepth(self):
    return self._receiverdepth

  def receiverdepth(self, val):
    """
    List of Double

    
    the receiver depth in km for stations not at the surface
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{receiverdepth} must be a list, not {val}")
    self._receiverdepth = val
    return self

  def get_scat(self):
    return self._scatter

  def scat(self, val):
    """
    List of Double

    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scatter in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scat} must be a list, not {val}")
    self._scatter = val
    return self

  def get_scatter(self):
    return self._scatter

  def scatter(self, val):
    """
    List of Double

    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scatter} must be a list, not {val}")
    self._scatter = val
    return self

  def get_p(self):
    return self._phase

  def p(self, val):
    """
    List of String

    
    seismic phase names
    Also known as --phase in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{p} must be a list, not {val}")
    self._phase = val
    return self

  def get_phase(self):
    return self._phase

  def phase(self, val):
    """
    List of String

    
    seismic phase names
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phase} must be a list, not {val}")
    self._phase = val
    return self

  def get_ph(self):
    return self._phase

  def ph(self, val):
    """
    List of String

    
    seismic phase names
    Also known as --phase in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{ph} must be a list, not {val}")
    self._phase = val
    return self

  def get_phasefile(self):
    return self._phasefile

  def phasefile(self, val):
    """
    List of String

    
    read list of phase names from file
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phasefile} must be a list, not {val}")
    self._phasefile = val
    return self

  def get_header(self):
    return self._header

  def header(self, val):
    """
    String
    
    reads depth and distance spacing data from a LOCSAT style file.
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

