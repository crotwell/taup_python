class CurveQuery:
  def __init__(self):
    self.toolname= "curve"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phase=[]
    self._phasefile=[]
    self._attenuationfreq=None
    self._numattenuationfreq=None
    self._strikediprake=[]
    self._mw=None
    self._az=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._color=None
    self._legend=None
    self._xaxis=None
    self._yaxis=None
    self._xminmax=None
    self._yminmax=None
    self._xabs=None
    self._yabs=None
    self._xlog=None
    self._ylog=None
    self._rel=None
    self._reddeg=None
    self._redkm=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_model(self):
    return self._model

  def model(self, val):
    """
    String
    
    use velocity model "modelName" for calculations. 
    Default is iasp91. Other builtin models include prem, ak135, ak135fcont, and ak135favg.
    Also known as --mod and --model in command line.
    """
    self._model = val
    return self

  def get_receiverdepth(self):
    return self._receiverdepth

  def receiverdepth(self, val):
    """
    List
    
    the receiver depth in km for stations not at the surface
    Also known as --stadepth and --receiverdepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{receiverdepth} must be a list, not {val}")
    self._receiverdepth = val
    return self

  def get_scatter(self):
    return self._scatter

  def scatter(self, val):
    """
    List
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Also known as --scat and --scatter in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{scatter} must be a list, not {val}")
    self._scatter = val
    return self

  def get_sourcedepth(self):
    return self._sourcedepth

  def sourcedepth(self, val):
    """
    List
    
    source depth in km
    Also known as -h and --sourcedepth in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sourcedepth} must be a list, not {val}")
    self._sourcedepth = val
    return self

  def get_phase(self):
    return self._phase

  def phase(self, val):
    """
    List
    
    seismic phase names
    Also known as -p and --phase in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phase} must be a list, not {val}")
    self._phase = val
    return self

  def get_phasefile(self):
    return self._phasefile

  def phasefile(self, val):
    """
    List
    
    read list of phase names from file
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phasefile} must be a list, not {val}")
    self._phasefile = val
    return self

  def get_attenuationfreq(self):
    return self._attenuationfreq

  def attenuationfreq(self, val):
    """
    Float
    
    attenuation frequency for amplitude calculations, default is 1.0
    """
    self._attenuationfreq = val
    return self

  def get_numattenuationfreq(self):
    return self._numattenuationfreq

  def numattenuationfreq(self, val):
    """
    Integer
    
     number attenuation frequencies for amplitude calculations, default is 64
    """
    self._numattenuationfreq = val
    return self

  def get_strikediprake(self):
    return self._strikediprake

  def strikediprake(self, val):
    """
    List
    
    fault strike, dip and rake for amplitude calculations. If not given radiation pattern is unity in all directions.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{strikediprake} must be a list, not {val}")
    self._strikediprake = val
    return self

  def get_mw(self):
    return self._mw

  def mw(self, val):
    """
    Float
    
    scale amplitude by source moment magnitude, default is 4.0
    """
    self._mw = val
    return self

  def get_az(self):
    return self._az

  def az(self, val):
    """
    Double
    
    azimuth in degrees, for amp calculations
    """
    self._az = val
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

  def get_color(self):
    return self._color

  def color(self, val):
    """
    edu.sc.seis.TauP.cmdline.args.ColorType
    
    style of coloring for paths and wavefronts, one of: auto, wavetype, phase, none
    """
    self._color = val
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

  def get_xaxis(self):
    return self._xaxis

  def xaxis(self, val):
    """
    edu.sc.seis.TauP.AxisType
    
    X axis data type, default is degree180, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Also known as -x and --xaxis in command line.
    """
    self._xaxis = val
    return self

  def get_yaxis(self):
    return self._yaxis

  def yaxis(self, val):
    """
    edu.sc.seis.TauP.AxisType
    
    Y axis data type, default is time, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Also known as -y and --yaxis in command line.
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

  def get_xabs(self):
    return self._xabs

  def xabs(self, val):
    """
    Boolean
    
    X axis is absolute value
    """
    self._xabs = val
    return self

  def get_yabs(self):
    return self._yabs

  def yabs(self, val):
    """
    Boolean
    
    Y axis is absolute value
    """
    self._yabs = val
    return self

  def get_xlog(self):
    return self._xlog

  def xlog(self, val):
    """
    Boolean
    
    X axis is log
    """
    self._xlog = val
    return self

  def get_ylog(self):
    return self._ylog

  def ylog(self, val):
    """
    Boolean
    
    Y axis is log
    """
    self._ylog = val
    return self

  def get_rel(self):
    return self._rel

  def rel(self, val):
    """
    String
    
    plot relative to the given phase, no effect unless distance/time
    """
    self._rel = val
    return self

  def get_reddeg(self):
    return self._reddeg

  def reddeg(self, val):
    """
    Double
    
    outputs curves with a reducing velocity (deg/sec), no effect if axis is not distance-like/time
    """
    self._reddeg = val
    return self

  def get_redkm(self):
    return self._redkm

  def redkm(self, val):
    """
    Double
    
    outputs curves with a reducing velocity (km/sec), no effect if axis is not distance-like/time
    """
    self._redkm = val
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
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._sourcedepth) > 0:
      params["sourcedepth"] = self._sourcedepth
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    if self._attenuationfreq is not None:
      params["attenuationfreq"] = self._attenuationfreq
    if self._numattenuationfreq is not None:
      params["numattenuationfreq"] = self._numattenuationfreq
    if len(self._strikediprake) > 0:
      params["strikediprake"] = self._strikediprake
    if self._mw is not None:
      params["mw"] = self._mw
    if self._az is not None:
      params["az"] = self._az
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._color is not None:
      params["color"] = self._color
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
    if self._xabs is not None:
      params["xabs"] = self._xabs
    if self._yabs is not None:
      params["yabs"] = self._yabs
    if self._xlog is not None:
      params["xlog"] = self._xlog
    if self._ylog is not None:
      params["ylog"] = self._ylog
    if self._rel is not None:
      params["rel"] = self._rel
    if self._reddeg is not None:
      params["reddeg"] = self._reddeg
    if self._redkm is not None:
      params["redkm"] = self._redkm
    return params

