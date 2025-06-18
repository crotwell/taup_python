class DisconQuery:
  def __init__(self):
    self.toolname= "discon"

    self._nd=[]
    self._tvel=[]
    self._model=[]

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  @property
  def nd(self):
    """
    List
    
    "named discontinuities" velocity file
    """
    return self._nd

  @nd.setter
  def nd(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{nd} must be a list, not {val}")
    self._nd = val

  @property
  def tvel(self):
    """
    List
    
    ".tvel" velocity file, ala ttimes
    """
    return self._tvel

  @tvel.setter
  def tvel(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{tvel} must be a list, not {val}")
    self._tvel = val

  @property
  def model(self):
    """
    List
    
    use velocity model "modelname" for calculations, format is guessed.
    Also known as --mod and --model in command line.
    """
    return self._model

  @model.setter
  def model(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{model} must be a list, not {val}")
    self._model = val


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if len(self._nd) > 0:
      params["nd"] = self._nd
    if len(self._tvel) > 0:
      params["tvel"] = self._tvel
    if len(self._model) > 0:
      params["model"] = self._model
    return params

