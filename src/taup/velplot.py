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
    self._yminmax=None
    self._xminmax=None
    self._yaxis=None
    self._xaxis=None

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

  def get_nameddiscon(self):
    """
    returns current value of nameddiscon as a Boolean
    """
    return self._nameddiscon

  def nameddiscon(self, val):
    """
    Sets the nameddiscon parameter, of type Boolean    
    outputs as .nd named discontinuity model file

    :param val: value to set nameddiscon to
    """
    self._nameddiscon = val
    return self

  def get_mapwidth(self):
    """
    returns current value of mapwidth as a Float
    """
    return self._mapwidth

  def mapwidth(self, val):
    """
    Sets the mapwidth parameter, of type Float    
    plot width in units from --mapwidthunit.

    :param val: value to set mapwidth to
    """
    self._mapwidth = val
    return self

  def get_mapwidthunit(self):
    """
    returns current value of mapwidthunit as a String
    """
    return self._mapwidthunit

  def mapwidthunit(self, val):
    """
    Sets the mapwidthunit parameter, of type String    
    plot width unit, i for inch, c for cm or p for px.

    :param val: value to set mapwidthunit to
    """
    self._mapwidthunit = val
    return self

  def get_legend(self):
    """
    returns current value of legend as a Boolean
    """
    return self._legend

  def legend(self, val):
    """
    Sets the legend parameter, of type Boolean    
    create a legend

    :param val: value to set legend to
    """
    self._legend = val
    return self

  def get_yminmax(self):
    """
    returns current value of yminmax as a [D
    """
    return self._yminmax

  def yminmax(self, val):
    """
    Sets the yminmax parameter, of type [D    
    min and max y axis for plotting

    :param val: value to set yminmax to
    """
    self._yminmax = val
    return self

  def get_xminmax(self):
    """
    returns current value of xminmax as a [D
    """
    return self._xminmax

  def xminmax(self, val):
    """
    Sets the xminmax parameter, of type [D    
    min and max x axis for plotting

    :param val: value to set xminmax to
    """
    self._xminmax = val
    return self

  def get_y(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._yaxis

  def y(self, val):
    """
    Sets the yaxis parameter, of type edu.sc.seis.TauP.ModelAxisType    
    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.
    Also known as --yaxis in command line.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self

  def get_yaxis(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._yaxis

  def yaxis(self, val):
    """
    Sets the yaxis parameter, of type edu.sc.seis.TauP.ModelAxisType    
    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self

  def get_x(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._xaxis

  def x(self, val):
    """
    Sets the xaxis parameter, of type edu.sc.seis.TauP.ModelAxisType    
    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.
    Also known as --xaxis in command line.

    :param val: value to set xaxis to
    """
    self._xaxis = val
    return self

  def get_xaxis(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._xaxis

  def xaxis(self, val):
    """
    Sets the xaxis parameter, of type edu.sc.seis.TauP.ModelAxisType    
    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.

    :param val: value to set xaxis to
    """
    self._xaxis = val
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
    if self._nameddiscon is not None:
      params["nameddiscon"] = self._nameddiscon
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._legend is not None:
      params["legend"] = self._legend
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    return params

