class VelplotQuery:
  def __init__(self):
    self.toolname= "velplot"

    self._model=[]
    self._nd=[]
    self._tvel=[]
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


  def get_mod(self):
    return self._model

  def mod(self, val):
    """
    List of String

    
    use velocity model "modelname" for calculations, format is guessed.
    Also known as --model in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{mod} must be a list, not {val}")
    self._model = val
    return self

  def get_model(self):
    return self._model

  def model(self, val):
    """
    List of String

    
    use velocity model "modelname" for calculations, format is guessed.
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

  def get_nameddiscon(self):
    return self._nameddiscon

  def nameddiscon(self, val):
    """
    Boolean
    
    outputs as .nd named discontinuity model file
    """
    self._nameddiscon = val
    return self

  def get_mapwidth(self):
    return self._mapwidth

  def mapwidth(self, val):
    """
    Float
    
    plot width in units from --mapwidthunit.
    """
    self._mapwidth = val
    return self

  def get_mapwidthunit(self):
    return self._mapwidthunit

  def mapwidthunit(self, val):
    """
    String
    
    plot width unit, i for inch, c for cm or p for px.
    """
    self._mapwidthunit = val
    return self

  def get_legend(self):
    return self._legend

  def legend(self, val):
    """
    Boolean
    
    create a legend
    """
    self._legend = val
    return self

  def get_x(self):
    return self._xaxis

  def x(self, val):
    """
    edu.sc.seis.TauP.ModelAxisType
    
    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.
    Also known as --xaxis in command line.
    """
    self._xaxis = val
    return self

  def get_xaxis(self):
    return self._xaxis

  def xaxis(self, val):
    """
    edu.sc.seis.TauP.ModelAxisType
    
    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.
    """
    self._xaxis = val
    return self

  def get_y(self):
    return self._yaxis

  def y(self, val):
    """
    edu.sc.seis.TauP.ModelAxisType
    
    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.
    Also known as --yaxis in command line.
    """
    self._yaxis = val
    return self

  def get_yaxis(self):
    return self._yaxis

  def yaxis(self, val):
    """
    edu.sc.seis.TauP.ModelAxisType
    
    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.
    """
    self._yaxis = val
    return self

  def get_xminmax(self):
    return self._xminmax

  def xminmax(self, val):
    """
    [D
    
    min and max x axis for plotting
    """
    self._xminmax = val
    return self

  def get_yminmax(self):
    return self._yminmax

  def yminmax(self, val):
    """
    [D
    
    min and max y axis for plotting
    """
    self._yminmax = val
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

