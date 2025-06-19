class DisconQuery:
  def __init__(self):
    self.toolname= "discon"

    self._model=[]
    self._nd=[]
    self._tvel=[]

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_model(self):
    return self._model

  def model(self, val):
    """
    List of String

    
    use velocity model "modelname" for calculations, format is guessed.
    Also known as --mod and --model in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{model} must be a list, not {val}")
    self._model = val
    return self

  def get_nd(self):
    return self._nd

  def nd(self, val):
    """
    List of String

    
    "named discontinuities" velocity file
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{nd} must be a list, not {val}")
    self._nd = val
    return self

  def get_tvel(self):
    return self._tvel

  def tvel(self, val):
    """
    List of String

    
    ".tvel" velocity file, ala ttimes
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{tvel} must be a list, not {val}")
    self._tvel = val
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if len(self._model) > 0:
      params["model"] = self._model
    if len(self._nd) > 0:
      params["nd"] = self._nd
    if len(self._tvel) > 0:
      params["tvel"] = self._tvel
    return params

