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


  def get_nd(self):
    """
    returns current value of nd as a String
    """
    return self._nd

  def nd(self, val):
    """
    Sets the nd parameter, of type String    
    "named discontinuities" velocity file

    :param val: value to set nd to
    """
    self._nd = val
    return self

  def get_tvel(self):
    """
    returns current value of tvel as a String
    """
    return self._tvel

  def tvel(self, val):
    """
    Sets the tvel parameter, of type String    
    ".tvel" velocity file, ala ttimes

    :param val: value to set tvel to
    """
    self._tvel = val
    return self

  def get_mod(self):
    """
    returns current value of model as a String
    """
    return self._model

  def mod(self, val):
    """
    Sets the model parameter, of type String    
    use velocity model "modelname" for calculations, format is guessed.
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
    use velocity model "modelname" for calculations, format is guessed.

    :param val: value to set model to
    """
    self._model = val
    return self

  def get_ndmerge(self):
    """
    returns current value of ndmerge as a String
    """
    return self._ndmerge

  def ndmerge(self, val):
    """
    Sets the ndmerge parameter, of type String    
    "named discontinuities" velocity file to merge

    :param val: value to set ndmerge to
    """
    self._ndmerge = val
    return self

  def get_tvelmerge(self):
    """
    returns current value of tvelmerge as a String
    """
    return self._tvelmerge

  def tvelmerge(self, val):
    """
    Sets the tvelmerge parameter, of type String    
    ".tvel" velocity file to merge, ala ttimes

    :param val: value to set tvelmerge to
    """
    self._tvelmerge = val
    return self

  def get_modmerge(self):
    """
    returns current value of modmerge as a String
    """
    return self._modmerge

  def modmerge(self, val):
    """
    Sets the modmerge parameter, of type String    
    velocity file to merge, format is guessed

    :param val: value to set modmerge to
    """
    self._modmerge = val
    return self

  def get_smoothtop(self):
    """
    returns current value of smoothtop as a Boolean
    """
    return self._smoothtop

  def smoothtop(self, val):
    """
    Sets the smoothtop parameter, of type Boolean    
    smooth merge at top

    :param val: value to set smoothtop to
    """
    self._smoothtop = val
    return self

  def get_smoothbot(self):
    """
    returns current value of smoothbot as a Boolean
    """
    return self._smoothbot

  def smoothbot(self, val):
    """
    Sets the smoothbot parameter, of type Boolean    
    smooth merge at bottom

    :param val: value to set smoothbot to
    """
    self._smoothbot = val
    return self

  def get_elev(self):
    """
    returns current value of elev as a Float
    """
    return self._elev

  def elev(self, val):
    """
    Sets the elev parameter, of type Float    
    increase topmost layer by elevation (meters)

    :param val: value to set elev to
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

