class VelplotQuery:
  def __init__(self):
    self.toolname= "velplot"

    self._nd=[]
    self._tvel=[]
    self._model=[]
    self._nameddiscon=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._legend=None
    self._xaxis=None
    self._yaxis=None
    self._xminmax=None
    self._yminmax=None

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

  @property
  def nameddiscon(self):
    """
    Boolean
    
    outputs as .nd named discontinuity model file
    """
    return self._nameddiscon

  @nameddiscon.setter
  def nameddiscon(self, val):
    self._nameddiscon = val

  @property
  def mapwidth(self):
    """
    Float
    
    plot width in units from --mapwidthunit.
    """
    return self._mapwidth

  @mapwidth.setter
  def mapwidth(self, val):
    self._mapwidth = val

  @property
  def mapwidthunit(self):
    """
    String
    
    plot width unit, i for inch, c for cm or p for px.
    """
    return self._mapwidthunit

  @mapwidthunit.setter
  def mapwidthunit(self, val):
    self._mapwidthunit = val

  @property
  def legend(self):
    """
    Boolean
    
    create a legend
    """
    return self._legend

  @legend.setter
  def legend(self, val):
    self._legend = val

  @property
  def xaxis(self):
    """
    edu.sc.seis.TauP.ModelAxisType
    
    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.
    Also known as -x and --xaxis in command line.
    """
    return self._xaxis

  @xaxis.setter
  def xaxis(self, val):
    self._xaxis = val

  @property
  def yaxis(self):
    """
    edu.sc.seis.TauP.ModelAxisType
    
    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.
    Also known as -y and --yaxis in command line.
    """
    return self._yaxis

  @yaxis.setter
  def yaxis(self, val):
    self._yaxis = val

  @property
  def xminmax(self):
    """
    [D
    
    min and max x axis for plotting
    """
    return self._xminmax

  @xminmax.setter
  def xminmax(self, val):
    self._xminmax = val

  @property
  def yminmax(self):
    """
    [D
    
    min and max y axis for plotting
    """
    return self._yminmax

  @yminmax.setter
  def yminmax(self, val):
    self._yminmax = val


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
    if self._nameddiscon is not None:
      params["nameddiscon"] = self._nameddiscon
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._legend is not None:
      params["legend"] = self._legend
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
    return params

