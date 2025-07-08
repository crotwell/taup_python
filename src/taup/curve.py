class CurveQuery:
  def __init__(self):
    self.toolname= "curve"

    self._attenuationfreq=None
    self._az=None
    self._color=None
    self._legend=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._model=None
    self._mw=None
    self._numattenuationfreq=None
    self._phase=[]
    self._phasefile=[]
    self._receiverdepth=[]
    self._reddeg=None
    self._redkm=None
    self._rel=None
    self._scatter=[]
    self._sourcedepth=[]
    self._strikediprake=[]
    self._xabs=None
    self._xaxis=None
    self._xlog=None
    self._xminmax=None
    self._yabs=None
    self._yaxis=None
    self._ylog=None
    self._yminmax=None

  def calc(self, taupServer):
    """
    Sends all params to the server, returns the result parsed from JSON.
    """
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def calcGmt(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of gmt.
    """
    params = self.create_params()
    return taupServer.queryGmt(params, self.toolname)


  def calcHtml(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of html.
    """
    params = self.create_params()
    return taupServer.queryHtml(params, self.toolname)


  def calcSvg(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of svg.
    """
    params = self.create_params()
    return taupServer.querySvg(params, self.toolname)


  def calcText(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of text.
    """
    params = self.create_params()
    return taupServer.queryText(params, self.toolname)


  def get_attenuationfreq(self):
    """
    returns current value of attenuationfreq as a Float
    """
    return self._attenuationfreq

  def attenuationfreq(self, val):
    """
    Sets the attenuationfreq parameter, of type Float    
    attenuation frequency for amplitude calculations, default is 1.0
    Known as --attenuationfreq in command line.

    :param val: value to set attenuationfreq to
    """
    self._attenuationfreq = val
    return self

  def get_az(self):
    """
    returns current value of az as a Double
    """
    return self._az

  def az(self, val):
    """
    Sets the az parameter, of type Double    
    azimuth in degrees, for amp calculations
    Known as --az in command line.

    :param val: value to set az to
    """
    self._az = val
    return self

  def get_color(self):
    """
    returns current value of color as a edu.sc.seis.TauP.cmdline.args.ColorType
    """
    return self._color

  def color(self, val):
    """
    Sets the color parameter, of type edu.sc.seis.TauP.cmdline.args.ColorType    
    style of coloring for paths and wavefronts, one of: auto, wavetype, phase, none
    Known as --color in command line.

    :param val: value to set color to
    """
    self._color = val
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
    Known as --legend in command line.

    :param val: value to set legend to
    """
    self._legend = val
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
    Known as --mapwidth in command line.

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
    Known as --mapwidthunit in command line.

    :param val: value to set mapwidthunit to
    """
    self._mapwidthunit = val
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
    Known as --mod in command line.
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
    Known as --model in command line.

    :param val: value to set model to
    """
    self._model = val
    return self

  def get_mw(self):
    """
    returns current value of mw as a Float
    """
    return self._mw

  def mw(self, val):
    """
    Sets the mw parameter, of type Float    
    scale amplitude by source moment magnitude, default is 4.0
    Known as --mw in command line.

    :param val: value to set mw to
    """
    self._mw = val
    return self

  def get_numattenuationfreq(self):
    """
    returns current value of numattenuationfreq as a Integer
    """
    return self._numattenuationfreq

  def numattenuationfreq(self, val):
    """
    Sets the numattenuationfreq parameter, of type Integer    
     number attenuation frequencies for amplitude calculations, default is 64
    Known as --numattenuationfreq in command line.

    :param val: value to set numattenuationfreq to
    """
    self._numattenuationfreq = val
    return self

  def get_p(self):
    """
    returns current value of phase as a List
    """
    return self._phase

  def p(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.p( value )
    and 
    .xp( [ value ] )
    are equivalent. 
    
    seismic phase names
    Known as -p in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self


  def andP(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.p( value )
    and 
    .xp( [ value ] )
    are equivalent. 
    
    seismic phase names
    Known as -p in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_phase(self):
    """
    returns current value of phase as a List
    """
    return self._phase

  def phase(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phase( value )
    and 
    .xphase( [ value ] )
    are equivalent. 
    
    seismic phase names
    Known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self


  def andPhase(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phase( value )
    and 
    .xphase( [ value ] )
    are equivalent. 
    
    seismic phase names
    Known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_ph(self):
    """
    returns current value of phase as a List
    """
    return self._phase

  def ph(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.ph( value )
    and 
    .xph( [ value ] )
    are equivalent. 
    
    seismic phase names
    Known as --ph in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
    return self


  def andPh(self, val):
    """
    Sets the phase parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.ph( value )
    and 
    .xph( [ value ] )
    are equivalent. 
    
    seismic phase names
    Known as --ph in command line.
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_phasefile(self):
    """
    returns current value of phasefile as a List
    """
    return self._phasefile

  def phasefile(self, val):
    """
    Sets the phasefile parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phasefile( value )
    and 
    .xphasefile( [ value ] )
    are equivalent. 
    
    read list of phase names from file
    Known as --phasefile in command line.

    :param val: value to set phasefile to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phasefile = val
    return self


  def andPhasefile(self, val):
    """
    Sets the phasefile parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phasefile( value )
    and 
    .xphasefile( [ value ] )
    are equivalent. 
    
    read list of phase names from file
    Known as --phasefile in command line.

    :param val: value to set phasefile to
    """
    self._phasefile.append(val)
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
    Known as --stadepth in command line.
    Also known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self


  def andStadepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.stadepth( value )
    and 
    .xstadepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface
    Known as --stadepth in command line.
    Also known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    self._receiverdepth.append(val)
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
    Known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._receiverdepth = val
    return self


  def andReceiverdepth(self, val):
    """
    Sets the receiverdepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.receiverdepth( value )
    and 
    .xreceiverdepth( [ value ] )
    are equivalent. 
    
    the receiver depth in km for stations not at the surface
    Known as --receiverdepth in command line.

    :param val: value to set receiverdepth to
    """
    self._receiverdepth.append(val)
    return self

  def get_reddeg(self):
    """
    returns current value of reddeg as a Double
    """
    return self._reddeg

  def reddeg(self, val):
    """
    Sets the reddeg parameter, of type Double    
    outputs curves with a reducing velocity (deg/sec), no effect if axis is not distance-like/time
    Known as --reddeg in command line.

    :param val: value to set reddeg to
    """
    self._reddeg = val
    return self

  def get_redkm(self):
    """
    returns current value of redkm as a Double
    """
    return self._redkm

  def redkm(self, val):
    """
    Sets the redkm parameter, of type Double    
    outputs curves with a reducing velocity (km/sec), no effect if axis is not distance-like/time
    Known as --redkm in command line.

    :param val: value to set redkm to
    """
    self._redkm = val
    return self

  def get_rel(self):
    """
    returns current value of rel as a String
    """
    return self._rel

  def rel(self, val):
    """
    Sets the rel parameter, of type String    
    plot relative to the given phase, no effect unless distance/time
    Known as --rel in command line.

    :param val: value to set rel to
    """
    self._rel = val
    return self

  def get_scat(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scat(self, depth, degree):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Known as --scat in command line.
    Also known as --scatter in command line.

    :param val: value to set scatter to
    """
    self._scatter = [depth, degree]
    return self

  def get_scatter(self):
    """
    returns current value of scatter as a List
    """
    return self._scatter

  def scatter(self, depth, degree):
    """
    Sets the scatter parameter, of type List of Double
    
    scattering depth and distance in degrees, which may be negative. Only effects phases with 'o' or 'O' in the phase name.
    Known as --scatter in command line.

    :param val: value to set scatter to
    """
    self._scatter = [depth, degree]
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
    Known as -h in command line.
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sourcedepth = val
    return self


  def andH(self, val):
    """
    Sets the sourcedepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.h( value )
    and 
    .xh( [ value ] )
    are equivalent. 
    
    source depth in km
    Known as -h in command line.
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    self._sourcedepth.append(val)
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
    Known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sourcedepth = val
    return self


  def andSourcedepth(self, val):
    """
    Sets the sourcedepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.sourcedepth( value )
    and 
    .xsourcedepth( [ value ] )
    are equivalent. 
    
    source depth in km
    Known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    self._sourcedepth.append(val)
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
    Known as --evdepth in command line.
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sourcedepth = val
    return self


  def andEvdepth(self, val):
    """
    Sets the sourcedepth parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.evdepth( value )
    and 
    .xevdepth( [ value ] )
    are equivalent. 
    
    source depth in km
    Known as --evdepth in command line.
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    self._sourcedepth.append(val)
    return self

  def get_strikediprake(self):
    """
    returns current value of strikediprake as a List
    """
    return self._strikediprake

  def strikediprake(self, val):
    """
    Sets the strikediprake parameter, of type List of Float
    
    fault strike, dip and rake for amplitude calculations. If not given radiation pattern is unity in all directions.
    Known as --strikediprake in command line.

    :param val: value to set strikediprake to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"strikediprake() requires a list, not {val}")
    self._strikediprake = val
    return self


  def andStrikediprake(self, val):
    """
    Sets the strikediprake parameter, of type List of Float
    
    fault strike, dip and rake for amplitude calculations. If not given radiation pattern is unity in all directions.
    Known as --strikediprake in command line.

    :param val: value to set strikediprake to
    """
    self._strikediprake.append(val)
    return self

  def get_xabs(self):
    """
    returns current value of xabs as a Boolean
    """
    return self._xabs

  def xabs(self, val):
    """
    Sets the xabs parameter, of type Boolean    
    X axis is absolute value
    Known as --xabs in command line.

    :param val: value to set xabs to
    """
    self._xabs = val
    return self

  def get_x(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.AxisType
    """
    return self._xaxis

  def x(self, val):
    """
    Sets the xaxis parameter, of type edu.sc.seis.TauP.AxisType    
    X axis data type, default is degree180, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Known as -x in command line.
    Also known as --xaxis in command line.

    :param val: value to set xaxis to
    """
    self._xaxis = val
    return self

  def get_xaxis(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.AxisType
    """
    return self._xaxis

  def xaxis(self, val):
    """
    Sets the xaxis parameter, of type edu.sc.seis.TauP.AxisType    
    X axis data type, default is degree180, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Known as --xaxis in command line.

    :param val: value to set xaxis to
    """
    self._xaxis = val
    return self

  def get_xlog(self):
    """
    returns current value of xlog as a Boolean
    """
    return self._xlog

  def xlog(self, val):
    """
    Sets the xlog parameter, of type Boolean    
    X axis is log
    Known as --xlog in command line.

    :param val: value to set xlog to
    """
    self._xlog = val
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
    Known as --xminmax in command line.

    :param val: value to set xminmax to
    """
    self._xminmax = val
    return self

  def get_yabs(self):
    """
    returns current value of yabs as a Boolean
    """
    return self._yabs

  def yabs(self, val):
    """
    Sets the yabs parameter, of type Boolean    
    Y axis is absolute value
    Known as --yabs in command line.

    :param val: value to set yabs to
    """
    self._yabs = val
    return self

  def get_y(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.AxisType
    """
    return self._yaxis

  def y(self, val):
    """
    Sets the yaxis parameter, of type edu.sc.seis.TauP.AxisType    
    Y axis data type, default is time, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Known as -y in command line.
    Also known as --yaxis in command line.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self

  def get_yaxis(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.AxisType
    """
    return self._yaxis

  def yaxis(self, val):
    """
    Sets the yaxis parameter, of type edu.sc.seis.TauP.AxisType    
    Y axis data type, default is time, one of radian, radian180, degree, degree180, kilometer, kilometer180, rayparamrad, rayparamdeg, rayparamkm, time, tau, takeoffangle, incidentangle, turndepth, amp, amppsv, ampsh, geospread, refltran, refltranpsv, refltransh, index, tstar, attenuation, theta, energygeospread, pathlength, radiation, radiationpsv, radiationsh
    Known as --yaxis in command line.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self

  def get_ylog(self):
    """
    returns current value of ylog as a Boolean
    """
    return self._ylog

  def ylog(self, val):
    """
    Sets the ylog parameter, of type Boolean    
    Y axis is log
    Known as --ylog in command line.

    :param val: value to set ylog to
    """
    self._ylog = val
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
    Known as --yminmax in command line.

    :param val: value to set yminmax to
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
    if self._attenuationfreq is not None:
      params["attenuationfreq"] = self._attenuationfreq
    if self._az is not None:
      params["az"] = self._az
    if self._color is not None:
      params["color"] = self._color
    if self._legend is not None:
      params["legend"] = self._legend
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._model is not None:
      params["model"] = self._model
    if self._mw is not None:
      params["mw"] = self._mw
    if self._numattenuationfreq is not None:
      params["numattenuationfreq"] = self._numattenuationfreq
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if self._reddeg is not None:
      params["reddeg"] = self._reddeg
    if self._redkm is not None:
      params["redkm"] = self._redkm
    if self._rel is not None:
      params["rel"] = self._rel
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._sourcedepth) > 0:
      params["sourcedepth"] = self._sourcedepth
    if len(self._strikediprake) > 0:
      params["strikediprake"] = self._strikediprake
    if self._xabs is not None:
      params["xabs"] = self._xabs
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    if self._xlog is not None:
      params["xlog"] = self._xlog
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if self._yabs is not None:
      params["yabs"] = self._yabs
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    if self._ylog is not None:
      params["ylog"] = self._ylog
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
    return params

