class DisconQuery:
  def __init__(self):
    self.toolname= "discon"

    self._nd=[]
    self._tvel=[]
    self._model=[]

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_nd(self):
    """
    returns current value of nd as a List
    """
    return self._nd

  def nd(self, val):
    """
    Sets the nd parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.nd( value )
    and 
    .xnd( [ value ] )
    are equivalent. 
    
    "named discontinuities" velocity file

    :param val: value to set nd to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._nd = val
    return self

  def get_tvel(self):
    """
    returns current value of tvel as a List
    """
    return self._tvel

  def tvel(self, val):
    """
    Sets the tvel parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.tvel( value )
    and 
    .xtvel( [ value ] )
    are equivalent. 
    
    ".tvel" velocity file, ala ttimes

    :param val: value to set tvel to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._tvel = val
    return self

  def get_mod(self):
    """
    returns current value of model as a List
    """
    return self._model

  def mod(self, val):
    """
    Sets the model parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.mod( value )
    and 
    .xmod( [ value ] )
    are equivalent. 
    
    use velocity model "modelname" for calculations, format is guessed.
    Also known as --model in command line.

    :param val: value to set model to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._model = val
    return self

  def get_model(self):
    """
    returns current value of model as a List
    """
    return self._model

  def model(self, val):
    """
    Sets the model parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.model( value )
    and 
    .xmodel( [ value ] )
    are equivalent. 
    
    use velocity model "modelname" for calculations, format is guessed.

    :param val: value to set model to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._model = val
    return self


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

