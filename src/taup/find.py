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
    List of Double

    
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
    List of Double

    
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
    List of Double

    
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
    List of String

    
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
    List of String

    
    read list of phase names from file
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{phasefile} must be a list, not {val}")
    self._phasefile = val
    return self

  def get_showrayparam(self):
    return self._showrayparam

  def showrayparam(self, val):
    """
    Boolean
    
    show min and max ray parameter for each phase name
    """
    self._showrayparam = val
    return self

  def get_max(self):
    return self._max

  def max(self, val):
    """
    Integer
    
    Maximum number of reflections and phase conversion
    """
    self._max = val
    return self

  def get_rayparamdeg(self):
    return self._rayparamdeg

  def rayparamdeg(self, val):
    """
    [Ljava.lang.Double;
    
    only keep phases that overlap the given ray parameter range in s/deg
    """
    self._rayparamdeg = val
    return self

  def get_rayparamkm(self):
    return self._rayparamkm

  def rayparamkm(self, val):
    """
    [Ljava.lang.Double;
    
    only keep phases that overlap the given ray parameter range in s/km
    """
    self._rayparamkm = val
    return self

  def get_exclude(self):
    return self._exclude

  def exclude(self, val):
    """
    List of String

    
    Exclude boundaries from phase conversion or reflection interactions
    May be depth (within tol) or named boundary like moho, cmb, iocb
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exclude} must be a list, not {val}")
    self._exclude = val
    return self

  def get_onlynameddiscon(self):
    return self._onlynameddiscon

  def onlynameddiscon(self, val):
    """
    Boolean
    
    only interact with named discontinuities like moho, cmb, iocb
    """
    self._onlynameddiscon = val
    return self

  def get_pwaveonly(self):
    return self._pwaveonly

  def pwaveonly(self, val):
    """
    Boolean
    
    only P wave legs, no S
    """
    self._pwaveonly = val
    return self

  def get_swaveonly(self):
    return self._swaveonly

  def swaveonly(self, val):
    """
    Boolean
    
    only S wave legs, no P
    """
    self._swaveonly = val
    return self

  def get_time(self):
    return self._time

  def time(self, val):
    """
    List of Double

    
    find arrivals within the given range
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{time} must be a list, not {val}")
    self._time = val
    return self

  def get_deltatime(self):
    return self._deltatime

  def deltatime(self, val):
    """
    Double
    
    find arrivals within the +- deltatime, --times must have single time
    """
    self._deltatime = val
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

  def get_mw(self):
    return self._mw

  def mw(self, val):
    """
    Float
    
    scale amplitude by source moment magnitude, default is 4.0
    """
    self._mw = val
    return self

  def get_strikediprake(self):
    return self._strikediprake

  def strikediprake(self, val):
    """
    List of Float

    
    fault strike, dip and rake for amplitude calculations. If not given radiation pattern is unity in all directions.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{strikediprake} must be a list, not {val}")
    self._strikediprake = val
    return self

  def get_amp(self):
    return self._amp

  def amp(self, val):
    """
    Boolean
    
    show amplitude factor for each phase
    """
    self._amp = val
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

  def get_degree(self):
    return self._degree

  def degree(self, val):
    """
    List of Double

    
    distance in degrees
    Also known as --deg and --degree in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degree} must be a list, not {val}")
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

