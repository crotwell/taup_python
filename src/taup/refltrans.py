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
    self._x=None
    self._y=[]
    self._xminmax=None
    self._yminmax=None
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

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


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

  def get_mod(self):
    return self._model

  def mod(self, val):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    Also known as --model in command line.
    """
    self._model = val
    return self

  def get_model(self):
    return self._model

  def model(self, val):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    """
    self._model = val
    return self

  def get_stadepth(self):
    return self._receiverdepth

  def stadepth(self, val):
    """
    List of Double

    
    the receiver depth in km for stations not at the surface
    Also known as --receiverdepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{stadepth} must be a list, not {val}")
    self._receiverdepth = val
    return self

  def get_receiverdepth(self):
    return self._receiverdepth

  def receiverdepth(self, val):
    """
    List of Double

    
    the receiver depth in km for stations not at the surface
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{receiverdepth} must be a list, not {val}")
    self._receiverdepth = val
    return self

  def get_scat(self):
    return self._scatter

  def scat(self, val):
    """
    List of Double

    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scatter in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scat} must be a list, not {val}")
    self._scatter = val
    return self

  def get_scatter(self):
    return self._scatter

  def scatter(self, val):
    """
    List of Double

    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scatter} must be a list, not {val}")
    self._scatter = val
    return self

  def get_h(self):
    return self._sourcedepth

  def h(self, val):
    """
    List of Double

    
    source depth in km
    Also known as --sourcedepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{h} must be a list, not {val}")
    self._sourcedepth = val
    return self

  def get_sourcedepth(self):
    return self._sourcedepth

  def sourcedepth(self, val):
    """
    List of Double

    
    source depth in km
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sourcedepth} must be a list, not {val}")
    self._sourcedepth = val
    return self

  def get_evdepth(self):
    return self._sourcedepth

  def evdepth(self, val):
    """
    List of Double

    
    source depth in km
    Also known as --sourcedepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{evdepth} must be a list, not {val}")
    self._sourcedepth = val
    return self

  def get_depth(self):
    return self._depth

  def depth(self, val):
    """
    String
    
    Depth in model to get boundary parameters, may be number or name like moho.
    """
    self._depth = val
    return self

  def get_angles(self):
    return self._angles

  def angles(self, val):
    """
    Boolean
    
    all angle coefficients, like TpAngle
    """
    self._angles = val
    return self

  def get_x(self):
    return self._x

  def x(self, val):
    """
    edu.sc.seis.TauP.cmdline.TauP_ReflTransPlot$DegRayParam
    
    X axis data type, one of degree, rayparam, default is degree
    """
    self._x = val
    return self

  def get_y(self):
    return self._y

  def y(self, val):
    """
    List of edu.sc.seis.TauP.ReflTransAxisType

    
    Y axis data type, one or more of Rpp, Rps, Rsp, Rss, Tpp, Tps, Tsp, Tss, Rshsh, Tshsh, RppEnergy, TppEnergy, RpsEnergy, TpsEnergy, RspEnergy, TspEnergy, RssEnergy, TssEnergy, RshshEnergy, TshshEnergy, RpAngle, RsAngle, TpAngle, TsAngle, FreeRecFuncPr, FreeRecFuncSvr, FreeRecFuncPz, FreeRecFuncSvz, FreeRecFuncSh, default is all displacement coef.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{y} must be a list, not {val}")
    self._y = val
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

  def get_layer(self):
    return self._layer

  def layer(self, val):
    """
    [D
    
    inbound and transmitted layer parameters, vp, vs, rho, vp, vs, rho
    """
    self._layer = val
    return self

  def get_down(self):
    return self._down

  def down(self, val):
    """
    Boolean
    
    incident is downgoing
    """
    self._down = val
    return self

  def get_up(self):
    return self._up

  def up(self, val):
    """
    Boolean
    
    incident is upgoing, reverses the sense of the boundary
    """
    self._up = val
    return self

  def get_pwave(self):
    return self._pwave

  def pwave(self, val):
    """
    Boolean
    
    incident P wave
    """
    self._pwave = val
    return self

  def get_swave(self):
    return self._swave

  def swave(self, val):
    """
    Boolean
    
    incident S wave
    """
    self._swave = val
    return self

  def get_shwave(self):
    return self._shwave

  def shwave(self, val):
    """
    Boolean
    
    incident SH wave
    """
    self._shwave = val
    return self

  def get_energyflux(self):
    return self._energyflux

  def energyflux(self, val):
    """
    Boolean
    
    all energy flux coefficients, like TppEnergy
    """
    self._energyflux = val
    return self

  def get_fsrf(self):
    return self._fsrf

  def fsrf(self, val):
    """
    Boolean
    
    all free surface receiver functions, like FreeRecFuncPz
    """
    self._fsrf = val
    return self

  def get_abs(self):
    return self._abs

  def abs(self, val):
    """
    Boolean
    
    absolute value of amplitude factor
    """
    self._abs = val
    return self

  def get_anglestep(self):
    return self._anglestep

  def anglestep(self, val):
    """
    Double
    
    step in degrees when x is degrees
    """
    self._anglestep = val
    return self

  def get_rpstep(self):
    return self._rpstep

  def rpstep(self, val):
    """
    Double
    
    step in ray param when x is ray param
    """
    self._rpstep = val
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
    if self._x is not None:
      params["x"] = self._x
    if len(self._y) > 0:
      params["y"] = self._y
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
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
    return params

