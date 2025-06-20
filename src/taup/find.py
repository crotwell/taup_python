class FindQuery:
  def __init__(self):
    self.toolname= "find"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phase=[]
    self._phasefile=[]
    self._showrayparam=None
    self._max=None
    self._rayparamdeg=None
    self._rayparamkm=None
    self._exclude=[]
    self._onlynameddiscon=None
    self._pwaveonly=None
    self._swaveonly=None
    self._time=[]
    self._deltatime=None
    self._attenuationfreq=None
    self._numattenuationfreq=None
    self._mw=None
    self._strikediprake=[]
    self._amp=None
    self._az=None
    self._degree=[]

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


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
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
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

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
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
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phase = val
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

    :param val: value to set phasefile to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phasefile = val
    return self

  def get_showrayparam(self):
    """
    returns current value of showrayparam as a Boolean
    """
    return self._showrayparam

  def showrayparam(self, val):
    """
    Sets the showrayparam parameter, of type Boolean    
    show min and max ray parameter for each phase name

    :param val: value to set showrayparam to
    """
    self._showrayparam = val
    return self

  def get_max(self):
    """
    returns current value of max as a Integer
    """
    return self._max

  def max(self, val):
    """
    Sets the max parameter, of type Integer    
    Maximum number of reflections and phase conversion

    :param val: value to set max to
    """
    self._max = val
    return self

  def get_rayparamdeg(self):
    """
    returns current value of rayparamdeg as a [Ljava.lang.Double;
    """
    return self._rayparamdeg

  def rayparamdeg(self, val):
    """
    Sets the rayparamdeg parameter, of type [Ljava.lang.Double;    
    only keep phases that overlap the given ray parameter range in s/deg

    :param val: value to set rayparamdeg to
    """
    self._rayparamdeg = val
    return self

  def get_rayparamkm(self):
    """
    returns current value of rayparamkm as a [Ljava.lang.Double;
    """
    return self._rayparamkm

  def rayparamkm(self, val):
    """
    Sets the rayparamkm parameter, of type [Ljava.lang.Double;    
    only keep phases that overlap the given ray parameter range in s/km

    :param val: value to set rayparamkm to
    """
    self._rayparamkm = val
    return self

  def get_exclude(self):
    """
    returns current value of exclude as a List
    """
    return self._exclude

  def exclude(self, val):
    """
    Sets the exclude parameter, of type List of String
    
    Exclude boundaries from phase conversion or reflection interactions
    May be depth (within tol) or named boundary like moho, cmb, iocb

    :param val: value to set exclude to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"exclude() requires a list, not {val}")
    self._exclude = val
    return self

  def get_onlynameddiscon(self):
    """
    returns current value of onlynameddiscon as a Boolean
    """
    return self._onlynameddiscon

  def onlynameddiscon(self, val):
    """
    Sets the onlynameddiscon parameter, of type Boolean    
    only interact with named discontinuities like moho, cmb, iocb

    :param val: value to set onlynameddiscon to
    """
    self._onlynameddiscon = val
    return self

  def get_pwaveonly(self):
    """
    returns current value of pwaveonly as a Boolean
    """
    return self._pwaveonly

  def pwaveonly(self, val):
    """
    Sets the pwaveonly parameter, of type Boolean    
    only P wave legs, no S

    :param val: value to set pwaveonly to
    """
    self._pwaveonly = val
    return self

  def get_swaveonly(self):
    """
    returns current value of swaveonly as a Boolean
    """
    return self._swaveonly

  def swaveonly(self, val):
    """
    Sets the swaveonly parameter, of type Boolean    
    only S wave legs, no P

    :param val: value to set swaveonly to
    """
    self._swaveonly = val
    return self

  def get_time(self):
    """
    returns current value of time as a List
    """
    return self._time

  def time(self, val):
    """
    Sets the time parameter, of type List of Double
    
    find arrivals within the given range

    :param val: value to set time to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"time() requires a list, not {val}")
    self._time = val
    return self

  def get_deltatime(self):
    """
    returns current value of deltatime as a Double
    """
    return self._deltatime

  def deltatime(self, val):
    """
    Sets the deltatime parameter, of type Double    
    find arrivals within the +- deltatime, --times must have single time

    :param val: value to set deltatime to
    """
    self._deltatime = val
    return self

  def get_attenuationfreq(self):
    """
    returns current value of attenuationfreq as a Float
    """
    return self._attenuationfreq

  def attenuationfreq(self, val):
    """
    Sets the attenuationfreq parameter, of type Float    
    attenuation frequency for amplitude calculations, default is 1.0

    :param val: value to set attenuationfreq to
    """
    self._attenuationfreq = val
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

    :param val: value to set numattenuationfreq to
    """
    self._numattenuationfreq = val
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

    :param val: value to set mw to
    """
    self._mw = val
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

    :param val: value to set strikediprake to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"strikediprake() requires a list, not {val}")
    self._strikediprake = val
    return self

  def get_amp(self):
    """
    returns current value of amp as a Boolean
    """
    return self._amp

  def amp(self, val):
    """
    Sets the amp parameter, of type Boolean    
    show amplitude factor for each phase

    :param val: value to set amp to
    """
    self._amp = val
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

    :param val: value to set az to
    """
    self._az = val
    return self

  def get_deg(self):
    """
    returns current value of degree as a List
    """
    return self._degree

  def deg(self, val):
    """
    Sets the degree parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.deg( value )
    and 
    .xdeg( [ value ] )
    are equivalent. 
    
    distance in degrees
    Also known as --degree in command line.

    :param val: value to set degree to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._degree = val
    return self

  def get_degree(self):
    """
    returns current value of degree as a List
    """
    return self._degree

  def degree(self, val):
    """
    Sets the degree parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.degree( value )
    and 
    .xdegree( [ value ] )
    are equivalent. 
    
    distance in degrees

    :param val: value to set degree to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._degree = val
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
    if self._showrayparam is not None:
      params["showrayparam"] = self._showrayparam
    if self._max is not None:
      params["max"] = self._max
    if self._rayparamdeg is not None:
      params["rayparamdeg"] = self._rayparamdeg
    if self._rayparamkm is not None:
      params["rayparamkm"] = self._rayparamkm
    if len(self._exclude) > 0:
      params["exclude"] = self._exclude
    if self._onlynameddiscon is not None:
      params["onlynameddiscon"] = self._onlynameddiscon
    if self._pwaveonly is not None:
      params["pwaveonly"] = self._pwaveonly
    if self._swaveonly is not None:
      params["swaveonly"] = self._swaveonly
    if len(self._time) > 0:
      params["time"] = self._time
    if self._deltatime is not None:
      params["deltatime"] = self._deltatime
    if self._attenuationfreq is not None:
      params["attenuationfreq"] = self._attenuationfreq
    if self._numattenuationfreq is not None:
      params["numattenuationfreq"] = self._numattenuationfreq
    if self._mw is not None:
      params["mw"] = self._mw
    if len(self._strikediprake) > 0:
      params["strikediprake"] = self._strikediprake
    if self._amp is not None:
      params["amp"] = self._amp
    if self._az is not None:
      params["az"] = self._az
    if len(self._degree) > 0:
      params["degree"] = self._degree
    return params

