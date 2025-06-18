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
    self._x=None
    self._y=[]
    self._xminmax=None
    self._yminmax=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


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
  def model(self):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    Also known as --mod and --model in command line.
    """
    return self._model

  @model.setter
  def model(self, val):
    self._model = val

  @property
  def receiverdepth(self):
    """
    List
    
    the receiver depth in km for stations not at the surface
    Also known as --stadepth and --receiverdepth in command line.
    """
    return self._receiverdepth

  @receiverdepth.setter
  def receiverdepth(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{receiverdepth} must be a list, not {val}")
    self._receiverdepth = val

  @property
  def scatter(self):
    """
    List
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scat and --scatter in command line.
    """
    return self._scatter

  @scatter.setter
  def scatter(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scatter} must be a list, not {val}")
    self._scatter = val

  @property
  def sourcedepth(self):
    """
    List
    
    source depth in km
    Also known as -h and --sourcedepth in command line.
    """
    return self._sourcedepth

  @sourcedepth.setter
  def sourcedepth(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sourcedepth} must be a list, not {val}")
    self._sourcedepth = val

  @property
  def depth(self):
    """
    String
    
    Depth in model to get boundary parameters, may be number or name like moho.
    """
    return self._depth

  @depth.setter
  def depth(self, val):
    self._depth = val

  @property
  def angles(self):
    """
    Boolean
    
    all angle coefficients, like TpAngle
    """
    return self._angles

  @angles.setter
  def angles(self, val):
    self._angles = val

  @property
  def layer(self):
    """
    [D
    
    inbound and transmitted layer parameters, vp, vs, rho, vp, vs, rho
    """
    return self._layer

  @layer.setter
  def layer(self, val):
    self._layer = val

  @property
  def down(self):
    """
    Boolean
    
    incident is downgoing
    """
    return self._down

  @down.setter
  def down(self, val):
    self._down = val

  @property
  def up(self):
    """
    Boolean
    
    incident is upgoing, reverses the sense of the boundary
    """
    return self._up

  @up.setter
  def up(self, val):
    self._up = val

  @property
  def pwave(self):
    """
    Boolean
    
    incident P wave
    """
    return self._pwave

  @pwave.setter
  def pwave(self, val):
    self._pwave = val

  @property
  def swave(self):
    """
    Boolean
    
    incident S wave
    """
    return self._swave

  @swave.setter
  def swave(self, val):
    self._swave = val

  @property
  def shwave(self):
    """
    Boolean
    
    incident SH wave
    """
    return self._shwave

  @shwave.setter
  def shwave(self, val):
    self._shwave = val

  @property
  def energyflux(self):
    """
    Boolean
    
    all energy flux coefficients, like TppEnergy
    """
    return self._energyflux

  @energyflux.setter
  def energyflux(self, val):
    self._energyflux = val

  @property
  def fsrf(self):
    """
    Boolean
    
    all free surface receiver functions, like FreeRecFuncPz
    """
    return self._fsrf

  @fsrf.setter
  def fsrf(self, val):
    self._fsrf = val

  @property
  def abs(self):
    """
    Boolean
    
    absolute value of amplitude factor
    """
    return self._abs

  @abs.setter
  def abs(self, val):
    self._abs = val

  @property
  def anglestep(self):
    """
    Double
    
    step in degrees when x is degrees
    """
    return self._anglestep

  @anglestep.setter
  def anglestep(self, val):
    self._anglestep = val

  @property
  def rpstep(self):
    """
    Double
    
    step in ray param when x is ray param
    """
    return self._rpstep

  @rpstep.setter
  def rpstep(self, val):
    self._rpstep = val

  @property
  def x(self):
    """
    edu.sc.seis.TauP.cmdline.TauP_ReflTransPlot$DegRayParam
    
    X axis data type, one of degree, rayparam, default is degree
    """
    return self._x

  @x.setter
  def x(self, val):
    self._x = val

  @property
  def y(self):
    """
    List
    
    Y axis data type, one or more of Rpp, Rps, Rsp, Rss, Tpp, Tps, Tsp, Tss, Rshsh, Tshsh, RppEnergy, TppEnergy, RpsEnergy, TpsEnergy, RspEnergy, TspEnergy, RssEnergy, TssEnergy, RshshEnergy, TshshEnergy, RpAngle, RsAngle, TpAngle, TsAngle, FreeRecFuncPr, FreeRecFuncSvr, FreeRecFuncPz, FreeRecFuncSvz, FreeRecFuncSh, default is all displacement coef.
    """
    return self._y

  @y.setter
  def y(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{y} must be a list, not {val}")
    self._y = val

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
    if self._x is not None:
      params["x"] = self._x
    if len(self._y) > 0:
      params["y"] = self._y
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
    return params

