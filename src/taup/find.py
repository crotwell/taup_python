class FindQuery:
  def __init__(self):
    self.toolname= "find"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phasefile=[]
    self._phase=[]
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
  def showrayparam(self):
    """
    Boolean
    
    show min and max ray parameter for each phase name
    """
    return self._showrayparam

  @showrayparam.setter
  def showrayparam(self, val):
    self._showrayparam = val

  @property
  def max(self):
    """
    Integer
    
    Maximum number of reflections and phase conversion
    """
    return self._max

  @max.setter
  def max(self, val):
    self._max = val

  @property
  def rayparamdeg(self):
    """
    [Ljava.lang.Double;
    
    only keep phases that overlap the given ray parameter range in s/deg
    """
    return self._rayparamdeg

  @rayparamdeg.setter
  def rayparamdeg(self, val):
    self._rayparamdeg = val

  @property
  def rayparamkm(self):
    """
    [Ljava.lang.Double;
    
    only keep phases that overlap the given ray parameter range in s/km
    """
    return self._rayparamkm

  @rayparamkm.setter
  def rayparamkm(self, val):
    self._rayparamkm = val

  @property
  def exclude(self):
    """
    List
    
    Exclude boundaries from phase conversion or reflection interactions
    May be depth (within tol) or named boundary like moho, cmb, iocb
    """
    return self._exclude

  @exclude.setter
  def exclude(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exclude} must be a list, not {val}")
    self._exclude = val

  @property
  def onlynameddiscon(self):
    """
    Boolean
    
    only interact with named discontinuities like moho, cmb, iocb
    """
    return self._onlynameddiscon

  @onlynameddiscon.setter
  def onlynameddiscon(self, val):
    self._onlynameddiscon = val

  @property
  def pwaveonly(self):
    """
    Boolean
    
    only P wave legs, no S
    """
    return self._pwaveonly

  @pwaveonly.setter
  def pwaveonly(self, val):
    self._pwaveonly = val

  @property
  def swaveonly(self):
    """
    Boolean
    
    only S wave legs, no P
    """
    return self._swaveonly

  @swaveonly.setter
  def swaveonly(self, val):
    self._swaveonly = val

  @property
  def time(self):
    """
    List
    
    find arrivals within the given range
    """
    return self._time

  @time.setter
  def time(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{time} must be a list, not {val}")
    self._time = val

  @property
  def deltatime(self):
    """
    Double
    
    find arrivals within the +- deltatime, --times must have single time
    """
    return self._deltatime

  @deltatime.setter
  def deltatime(self, val):
    self._deltatime = val

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
  def amp(self):
    """
    Boolean
    
    show amplitude factor for each phase
    """
    return self._amp

  @amp.setter
  def amp(self, val):
    self._amp = val

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
  def degree(self):
    """
    List
    
    distance in degrees
    Also known as --deg and --degree in command line.
    """
    return self._degree

  @degree.setter
  def degree(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degree} must be a list, not {val}")
    self._degree = val


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

