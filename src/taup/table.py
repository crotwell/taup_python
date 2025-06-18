class TableQuery:
  def __init__(self):
    self.toolname= "table"

    self._generic=None
    self._locsat=None
    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._phasefile=[]
    self._phase=[]
    self._header=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  @property
  def generic(self):
    """
    Boolean
    
    outputs as Text
    Also known as --text and --generic in command line.
    """
    return self._generic

  @generic.setter
  def generic(self, val):
    self._generic = val

  @property
  def locsat(self):
    """
    Boolean
    
    outputs as Locsat
    """
    return self._locsat

  @locsat.setter
  def locsat(self, val):
    self._locsat = val

  @property
  def model(self):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    Also known as --mod and --model in command line.
    """
    return self._model

  @model.setter
  def model(self, val):
    self._model = val

  @property
  def receiverdepth(self):
    """
    List
    
    the receiver depth in km for stations not at the surface
    Also known as --stadepth and --receiverdepth in command line.
    """
    return self._receiverdepth

  @receiverdepth.setter
  def receiverdepth(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{receiverdepth} must be a list, not {val}")
    self._receiverdepth = val

  @property
  def scatter(self):
    """
    List
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scat and --scatter in command line.
    """
    return self._scatter

  @scatter.setter
  def scatter(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scatter} must be a list, not {val}")
    self._scatter = val

  @property
  def phasefile(self):
    """
    List
    
    read list of phase names from file
    """
    return self._phasefile

  @phasefile.setter
  def phasefile(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phasefile} must be a list, not {val}")
    self._phasefile = val

  @property
  def phase(self):
    """
    List
    
    seismic phase names
    Also known as -p and --phase in command line.
    """
    return self._phase

  @phase.setter
  def phase(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phase} must be a list, not {val}")
    self._phase = val

  @property
  def header(self):
    """
    String
    
    reads depth and distance spacing data from a LOCSAT style file.
    """
    return self._header

  @header.setter
  def header(self, val):
    self._header = val


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
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if self._header is not None:
      params["header"] = self._header
    return params

