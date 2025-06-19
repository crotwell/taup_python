class RefltransQuery:
  def __init__(self):
    self.toolname= "refltrans"

    self._mapwidth=None
    self._mapwidthunit=None
    self._legend=None
    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._depth=None
    self._angles=None
    self._layer=None
    self._down=None
    self._up=None
    self._pwave=None
    self._swave=None
    self._shwave=None
    self._energyflux=None
    self._fsrf=None
    self._abs=None
    self._anglestep=None
    self._rpstep=None
    self._yminmax=None
    self._xminmax=None
    self._y=[]
    self._x=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


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

  def get_mod(self):
    """
    returns current value of model as a String
    """
    return self._model

  def mod(self, val):
    """
    Sets the model parameter, of type String    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
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
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.

    :param val: value to set model to
    """
    self._model = val
    return self

  def get_stadepth(self):
    """
    returns current value of receiverdepth as a List
    """
    return self._receiverdepth

  def stadepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.stadepth( value )
    and 
    .xstadepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface
    Also known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self

  def get_receiverdepth(self):
    """
    returns current value of receiverdepth as a List
    """
    return self._receiverdepth

  def receiverdepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.receiverdepth( value )
    and 
    .xreceiverdepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self

  def get_scat(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scat(self, val):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scatter in command line.

    :param val: value to set scatter to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"scat() requires a list, not {val}")
    self._scatter = val
    return self

  def get_scatter(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scatter(self, val):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.

    :param val: value to set scatter to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"scatter() requires a list, not {val}")
    self._scatter = val
    return self

  def get_h(self):
    """
    returns current value of sourcedepth as a List
    """
    return self._sourcedepth

  def h(self, val):
    """
    Sets the sourcedepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.h( value )
    and 
    .xh( [ value ] )
    are equivalent. 
    
    source depth in km
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sourcedepth = val
    return self

  def get_sourcedepth(self):
    """
    returns current value of sourcedepth as a List
    """
    return self._sourcedepth

  def sourcedepth(self, val):
    """
    Sets the sourcedepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.sourcedepth( value )
    and 
    .xsourcedepth( [ value ] )
    are equivalent. 
    
    source depth in km

    :param val: value to set sourcedepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sourcedepth = val
    return self

  def get_evdepth(self):
    """
    returns current value of sourcedepth as a List
    """
    return self._sourcedepth

  def evdepth(self, val):
    """
    Sets the sourcedepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.evdepth( value )
    and 
    .xevdepth( [ value ] )
    are equivalent. 
    
    source depth in km
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sourcedepth = val
    return self

  def get_depth(self):
    """
    returns current value of depth as a String
    """
    return self._depth

  def depth(self, val):
    """
    Sets the depth parameter, of type String    
    Depth in model to get boundary parameters, may be number or name like moho.

    :param val: value to set depth to
    """
    self._depth = val
    return self

  def get_angles(self):
    """
    returns current value of angles as a Boolean
    """
    return self._angles

  def angles(self, val):
    """
    Sets the angles parameter, of type Boolean    
    all angle coefficients, like TpAngle

    :param val: value to set angles to
    """
    self._angles = val
    return self

  def get_layer(self):
    """
    returns current value of layer as a [D
    """
    return self._layer

  def layer(self, val):
    """
    Sets the layer parameter, of type [D    
    inbound and transmitted layer parameters, vp, vs, rho, vp, vs, rho

    :param val: value to set layer to
    """
    self._layer = val
    return self

  def get_down(self):
    """
    returns current value of down as a Boolean
    """
    return self._down

  def down(self, val):
    """
    Sets the down parameter, of type Boolean    
    incident is downgoing

    :param val: value to set down to
    """
    self._down = val
    return self

  def get_up(self):
    """
    returns current value of up as a Boolean
    """
    return self._up

  def up(self, val):
    """
    Sets the up parameter, of type Boolean    
    incident is upgoing, reverses the sense of the boundary

    :param val: value to set up to
    """
    self._up = val
    return self

  def get_pwave(self):
    """
    returns current value of pwave as a Boolean
    """
    return self._pwave

  def pwave(self, val):
    """
    Sets the pwave parameter, of type Boolean    
    incident P wave

    :param val: value to set pwave to
    """
    self._pwave = val
    return self

  def get_swave(self):
    """
    returns current value of swave as a Boolean
    """
    return self._swave

  def swave(self, val):
    """
    Sets the swave parameter, of type Boolean    
    incident S wave

    :param val: value to set swave to
    """
    self._swave = val
    return self

  def get_shwave(self):
    """
    returns current value of shwave as a Boolean
    """
    return self._shwave

  def shwave(self, val):
    """
    Sets the shwave parameter, of type Boolean    
    incident SH wave

    :param val: value to set shwave to
    """
    self._shwave = val
    return self

  def get_energyflux(self):
    """
    returns current value of energyflux as a Boolean
    """
    return self._energyflux

  def energyflux(self, val):
    """
    Sets the energyflux parameter, of type Boolean    
    all energy flux coefficients, like TppEnergy

    :param val: value to set energyflux to
    """
    self._energyflux = val
    return self

  def get_fsrf(self):
    """
    returns current value of fsrf as a Boolean
    """
    return self._fsrf

  def fsrf(self, val):
    """
    Sets the fsrf parameter, of type Boolean    
    all free surface receiver functions, like FreeRecFuncPz

    :param val: value to set fsrf to
    """
    self._fsrf = val
    return self

  def get_abs(self):
    """
    returns current value of abs as a Boolean
    """
    return self._abs

  def abs(self, val):
    """
    Sets the abs parameter, of type Boolean    
    absolute value of amplitude factor

    :param val: value to set abs to
    """
    self._abs = val
    return self

  def get_anglestep(self):
    """
    returns current value of anglestep as a Double
    """
    return self._anglestep

  def anglestep(self, val):
    """
    Sets the anglestep parameter, of type Double    
    step in degrees when x is degrees

    :param val: value to set anglestep to
    """
    self._anglestep = val
    return self

  def get_rpstep(self):
    """
    returns current value of rpstep as a Double
    """
    return self._rpstep

  def rpstep(self, val):
    """
    Sets the rpstep parameter, of type Double    
    step in ray param when x is ray param

    :param val: value to set rpstep to
    """
    self._rpstep = val
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
    returns current value of y as a List
    """
    return self._y

  def y(self, val):
    """
    Sets the y parameter, of type List of edu.sc.seis.TauP.ReflTransAxisType
    
    Y axis data type, one or more of Rpp, Rps, Rsp, Rss, Tpp, Tps, Tsp, Tss, Rshsh, Tshsh, RppEnergy, TppEnergy, RpsEnergy, TpsEnergy, RspEnergy, TspEnergy, RssEnergy, TssEnergy, RshshEnergy, TshshEnergy, RpAngle, RsAngle, TpAngle, TsAngle, FreeRecFuncPr, FreeRecFuncSvr, FreeRecFuncPz, FreeRecFuncSvz, FreeRecFuncSh, default is all displacement coef.

    :param val: value to set y to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"y() requires a list, not {val}")
    self._y = val
    return self

  def get_x(self):
    """
    returns current value of x as a edu.sc.seis.TauP.cmdline.TauP_ReflTransPlot$DegRayParam
    """
    return self._x

  def x(self, val):
    """
    Sets the x parameter, of type edu.sc.seis.TauP.cmdline.TauP_ReflTransPlot$DegRayParam    
    X axis data type, one of degree, rayparam, default is degree

    :param val: value to set x to
    """
    self._x = val
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._legend is not None:
      params["legend"] = self._legend
    if self._model is not None:
      params["model"] = self._model
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._sourcedepth) > 0:
      params["sourcedepth"] = self._sourcedepth
    if self._depth is not None:
      params["depth"] = self._depth
    if self._angles is not None:
      params["angles"] = self._angles
    if self._layer is not None:
      params["layer"] = self._layer
    if self._down is not None:
      params["down"] = self._down
    if self._up is not None:
      params["up"] = self._up
    if self._pwave is not None:
      params["pwave"] = self._pwave
    if self._swave is not None:
      params["swave"] = self._swave
    if self._shwave is not None:
      params["shwave"] = self._shwave
    if self._energyflux is not None:
      params["energyflux"] = self._energyflux
    if self._fsrf is not None:
      params["fsrf"] = self._fsrf
    if self._abs is not None:
      params["abs"] = self._abs
    if self._anglestep is not None:
      params["anglestep"] = self._anglestep
    if self._rpstep is not None:
      params["rpstep"] = self._rpstep
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if len(self._y) > 0:
      params["y"] = self._y
    if self._x is not None:
      params["x"] = self._x
    return params

