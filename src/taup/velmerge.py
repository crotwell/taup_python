class VelmergeQuery:
  def __init__(self):
    self.toolname= "velmerge"

    self._nd=None
    self._tvel=None
    self._model=None
    self._ndmerge=None
    self._tvelmerge=None
    self._modmerge=None
    self._smoothtop=None
    self._smoothbot=None
    self._elev=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  @property
  def nd(self):
    """
    String
    
    "named discontinuities" velocity file
    """
    return self._nd

  @nd.setter
  def nd(self, val):
    self._nd = val

  @property
  def tvel(self):
    """
    String
    
    ".tvel" velocity file, ala ttimes
    """
    return self._tvel

  @tvel.setter
  def tvel(self, val):
    self._tvel = val

  @property
  def model(self):
    """
    String
    
    use velocity model "modelname" for calculations, format is guessed.
    Also known as --mod and --model in command line.
    """
    return self._model

  @model.setter
  def model(self, val):
    self._model = val

  @property
  def ndmerge(self):
    """
    String
    
    "named discontinuities" velocity file to merge
    """
    return self._ndmerge

  @ndmerge.setter
  def ndmerge(self, val):
    self._ndmerge = val

  @property
  def tvelmerge(self):
    """
    String
    
    ".tvel" velocity file to merge, ala ttimes
    """
    return self._tvelmerge

  @tvelmerge.setter
  def tvelmerge(self, val):
    self._tvelmerge = val

  @property
  def modmerge(self):
    """
    String
    
    velocity file to merge, format is guessed
    """
    return self._modmerge

  @modmerge.setter
  def modmerge(self, val):
    self._modmerge = val

  @property
  def smoothtop(self):
    """
    Boolean
    
    smooth merge at top
    """
    return self._smoothtop

  @smoothtop.setter
  def smoothtop(self, val):
    self._smoothtop = val

  @property
  def smoothbot(self):
    """
    Boolean
    
    smooth merge at bottom
    """
    return self._smoothbot

  @smoothbot.setter
  def smoothbot(self, val):
    self._smoothbot = val

  @property
  def elev(self):
    """
    Float
    
    increase topmost layer by elevation (meters)
    """
    return self._elev

  @elev.setter
  def elev(self, val):
    self._elev = val


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._nd is not None:
      params["nd"] = self._nd
    if self._tvel is not None:
      params["tvel"] = self._tvel
    if self._model is not None:
      params["model"] = self._model
    if self._ndmerge is not None:
      params["ndmerge"] = self._ndmerge
    if self._tvelmerge is not None:
      params["tvelmerge"] = self._tvelmerge
    if self._modmerge is not None:
      params["modmerge"] = self._modmerge
    if self._smoothtop is not None:
      params["smoothtop"] = self._smoothtop
    if self._smoothbot is not None:
      params["smoothbot"] = self._smoothbot
    if self._elev is not None:
      params["elev"] = self._elev
    return params

