class CurveQuery:
  def __init__(self):
    self.toolname= "curve"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phasefile=[]
    self._phase=[]
    self._attenuationfreq=None
    self._numattenuationfreq=None
    self._mw=None
    self._strikediprake=[]
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
  def phasefile(self):
    """
    List
    
    read list of phase names from file
    """
    return self._phasefile

  @phasefile.setter
  def phasefile(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phasefile} must be a list, not {val}")
    self._phasefile = val

  @property
  def phase(self):
    """
    List
    
    seismic phase names
    Also known as -p and --phase in command line.
    """
    return self._phase

  @phase.setter
  def phase(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phase} must be a list, not {val}")
    self._phase = val

  @property
  def attenuationfreq(self):
    """
    Float
    
    attenuation frequency for amplitude calculations, default is 1.0
    """
    return self._attenuationfreq

  @attenuationfreq.setter
  def attenuationfreq(self, val):
    self._attenuationfreq = val

  @property
  def numattenuationfreq(self):
    """
    Integer
    
     number attenuation frequencies for amplitude calculations, default is 64
    """
    return self._numattenuationfreq

  @numattenuationfreq.setter
  def numattenuationfreq(self, val):
    self._numattenuationfreq = val

  @property
  def mw(self):
    """
    Float
    
    scale amplitude by source moment magnitude, default is 4.0
    """
    return self._mw

  @mw.setter
  def mw(self, val):
    self._mw = val

  @property
  def strikediprake(self):
    """
    List
    
    fault strike, dip and rake for amplitude calculations. If not given radiation pattern is unity in all directions.
    """
    return self._strikediprake

  @strikediprake.setter
  def strikediprake(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{strikediprake} must be a list, not {val}")
    self._strikediprake = val

  @property
  def az(self):
    """
    Double
    
    azimuth in degrees, for amp calculations
    """
    return self._az

  @az.setter
  def az(self, val):
    self._az = val

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
  def color(self):
    """
    edu.sc.seis.TauP.cmdline.args.ColorType
    
    style of coloring for paths and wavefronts, one of: auto, wavetype, phase, none
    """
    return self._color

  @color.setter
  def color(self, val):
    self._color = val

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
    edu.sc.seis.TauP.AxisType
    
    X axis data type, default is degree180, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Also known as -x and --xaxis in command line.
    """
    return self._xaxis

  @xaxis.setter
  def xaxis(self, val):
    self._xaxis = val

  @property
  def yaxis(self):
    """
    edu.sc.seis.TauP.AxisType
    
    Y axis data type, default is time, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
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

  @property
  def xabs(self):
    """
    Boolean
    
    X axis is absolute value
    """
    return self._xabs

  @xabs.setter
  def xabs(self, val):
    self._xabs = val

  @property
  def yabs(self):
    """
    Boolean
    
    Y axis is absolute value
    """
    return self._yabs

  @yabs.setter
  def yabs(self, val):
    self._yabs = val

  @property
  def xlog(self):
    """
    Boolean
    
    X axis is log
    """
    return self._xlog

  @xlog.setter
  def xlog(self, val):
    self._xlog = val

  @property
  def ylog(self):
    """
    Boolean
    
    Y axis is log
    """
    return self._ylog

  @ylog.setter
  def ylog(self, val):
    self._ylog = val

  @property
  def rel(self):
    """
    String
    
    plot relative to the given phase, no effect unless distance/time
    """
    return self._rel

  @rel.setter
  def rel(self, val):
    self._rel = val

  @property
  def reddeg(self):
    """
    Double
    
    outputs curves with a reducing velocity (deg/sec), no effect if axis is not distance-like/time
    """
    return self._reddeg

  @reddeg.setter
  def reddeg(self, val):
    self._reddeg = val

  @property
  def redkm(self):
    """
    Double
    
    outputs curves with a reducing velocity (km/sec), no effect if axis is not distance-like/time
    """
    return self._redkm

  @redkm.setter
  def redkm(self, val):
    self._redkm = val


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
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if self._attenuationfreq is not None:
      params["attenuationfreq"] = self._attenuationfreq
    if self._numattenuationfreq is not None:
      params["numattenuationfreq"] = self._numattenuationfreq
    if self._mw is not None:
      params["mw"] = self._mw
    if len(self._strikediprake) > 0:
      params["strikediprake"] = self._strikediprake
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

