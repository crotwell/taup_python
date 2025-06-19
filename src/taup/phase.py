class PhaseQuery:
  def __init__(self):
    self.toolname= "phase"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phase=[]
    self._phasefile=[]

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


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

  def get_h(self):
    return self._sourcedepth

  def h(self, val):
    """
    List of Double

    
    source depth in km
    Also known as --sourcedepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{h} must be a list, not {val}")
    self._sourcedepth = val
    return self

  def get_sourcedepth(self):
    return self._sourcedepth

  def sourcedepth(self, val):
    """
    List of Double

    
    source depth in km
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sourcedepth} must be a list, not {val}")
    self._sourcedepth = val
    return self

  def get_evdepth(self):
    return self._sourcedepth

  def evdepth(self, val):
    """
    List of Double

    
    source depth in km
    Also known as --sourcedepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{evdepth} must be a list, not {val}")
    self._sourcedepth = val
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


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._model is not None:
      params["model"] = self._model
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._sourcedepth) > 0:
      params["sourcedepth"] = self._sourcedepth
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    return params

