class VelmergeQuery:
  def __init__(self):
    self.toolname= "velmerge"

    self._model=None
    self._nd=None
    self._tvel=None
    self._modmerge=None
    self._ndmerge=None
    self._tvelmerge=None
    self._smoothtop=None
    self._smoothbot=None
    self._elev=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_mod(self):
    return self._model

  def mod(self, val):
    """
    String
    
    use velocity model "modelname" for calculations, format is guessed.
    Also known as --model in command line.
    """
    self._model = val
    return self

  def get_model(self):
    return self._model

  def model(self, val):
    """
    String
    
    use velocity model "modelname" for calculations, format is guessed.
    """
    self._model = val
    return self

  def get_nd(self):
    return self._nd

  def nd(self, val):
    """
    String
    
    "named discontinuities" velocity file
    """
    self._nd = val
    return self

  def get_tvel(self):
    return self._tvel

  def tvel(self, val):
    """
    String
    
    ".tvel" velocity file, ala ttimes
    """
    self._tvel = val
    return self

  def get_modmerge(self):
    return self._modmerge

  def modmerge(self, val):
    """
    String
    
    velocity file to merge, format is guessed
    """
    self._modmerge = val
    return self

  def get_ndmerge(self):
    return self._ndmerge

  def ndmerge(self, val):
    """
    String
    
    "named discontinuities" velocity file to merge
    """
    self._ndmerge = val
    return self

  def get_tvelmerge(self):
    return self._tvelmerge

  def tvelmerge(self, val):
    """
    String
    
    ".tvel" velocity file to merge, ala ttimes
    """
    self._tvelmerge = val
    return self

  def get_smoothtop(self):
    return self._smoothtop

  def smoothtop(self, val):
    """
    Boolean
    
    smooth merge at top
    """
    self._smoothtop = val
    return self

  def get_smoothbot(self):
    return self._smoothbot

  def smoothbot(self, val):
    """
    Boolean
    
    smooth merge at bottom
    """
    self._smoothbot = val
    return self

  def get_elev(self):
    return self._elev

  def elev(self, val):
    """
    Float
    
    increase topmost layer by elevation (meters)
    """
    self._elev = val
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
    if self._nd is not None:
      params["nd"] = self._nd
    if self._tvel is not None:
      params["tvel"] = self._tvel
    if self._modmerge is not None:
      params["modmerge"] = self._modmerge
    if self._ndmerge is not None:
      params["ndmerge"] = self._ndmerge
    if self._tvelmerge is not None:
      params["tvelmerge"] = self._tvelmerge
    if self._smoothtop is not None:
      params["smoothtop"] = self._smoothtop
    if self._smoothbot is not None:
      params["smoothbot"] = self._smoothbot
    if self._elev is not None:
      params["elev"] = self._elev
    return params

