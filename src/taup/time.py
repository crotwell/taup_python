class TimeQuery:
  def __init__(self):
    self.toolname= "time"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phase=[]
    self._phasefile=[]
    self._degree=[]
    self._degreerange=[]
    self._kilometer=[]
    self._kilometerrange=[]
    self._exactdegree=[]
    self._exactdegreerange=[]
    self._exactkilometer=[]
    self._exactkilometerrange=[]
    self._takeoff=[]
    self._takeoffrange=[]
    self._incident=[]
    self._incidentrange=[]
    self._rayparamrad=[]
    self._rayparamdeg=[]
    self._rayparamkm=[]
    self._rayparamidx=[]
    self._allindex=None
    self._station=[]
    self._event=[]
    self._az=None
    self._baz=None
    self._geodetic=None
    self._geodeticflattening=None
    self._eid=[]
    self._sid=[]
    self._quakeml=None
    self._staxml=None
    self._onlyrayp=None
    self._onlytime=None
    self._onlyfirst=None
    self._attenuationfreq=None
    self._numattenuationfreq=None
    self._strikediprake=[]
    self._mw=None
    self._amp=None
    self._rel=[]

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

  def get_degree(self):
    return self._degree

  def degree(self, val):
    """
    List
    
    distance in degrees
    Also known as --deg and --degree in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degree} must be a list, not {val}")
    self._degree = val
    return self

  def get_degreerange(self):
    return self._degreerange

  def degreerange(self, val):
    """
    List
    
    regular distance range in degrees, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degreerange} must be a list, not {val}")
    self._degreerange = val
    return self

  def get_kilometer(self):
    return self._kilometer

  def kilometer(self, val):
    """
    List
    
    distance in kilometers along surface.
    Also known as --km and --kilometer in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{kilometer} must be a list, not {val}")
    self._kilometer = val
    return self

  def get_kilometerrange(self):
    return self._kilometerrange

  def kilometerrange(self, val):
    """
    List
    
    regular distance range in kilometers, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{kilometerrange} must be a list, not {val}")
    self._kilometerrange = val
    return self

  def get_exactdegree(self):
    return self._exactdegree

  def exactdegree(self, val):
    """
    List
    
    exact distance traveled in degrees, not 360-d
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactdegree} must be a list, not {val}")
    self._exactdegree = val
    return self

  def get_exactdegreerange(self):
    return self._exactdegreerange

  def exactdegreerange(self, val):
    """
    List
    
    regular distance range in exact degrees, not 360-deg, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactdegreerange} must be a list, not {val}")
    self._exactdegreerange = val
    return self

  def get_exactkilometer(self):
    return self._exactkilometer

  def exactkilometer(self, val):
    """
    List
    
    exact distance traveled in kilometers, not 360-k
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactkilometer} must be a list, not {val}")
    self._exactkilometer = val
    return self

  def get_exactkilometerrange(self):
    return self._exactkilometerrange

  def exactkilometerrange(self, val):
    """
    List
    
    regular distance range in kilometers, not 360-k, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactkilometerrange} must be a list, not {val}")
    self._exactkilometerrange = val
    return self

  def get_takeoff(self):
    return self._takeoff

  def takeoff(self, val):
    """
    List
    
    takeoff angle in degrees from the source, zero is down, 90 horizontal, 180 is up.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{takeoff} must be a list, not {val}")
    self._takeoff = val
    return self

  def get_takeoffrange(self):
    return self._takeoffrange

  def takeoffrange(self, val):
    """
    List
    
    regular range in takeoff angle in degrees, one of step; min,max or min,max,step. Default min is 0 and step is 10.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{takeoffrange} must be a list, not {val}")
    self._takeoffrange = val
    return self

  def get_incident(self):
    return self._incident

  def incident(self, val):
    """
    List
    
    incident angle in degrees at the receiver, zero is down, 90 horizontal, 180 is up.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{incident} must be a list, not {val}")
    self._incident = val
    return self

  def get_incidentrange(self):
    return self._incidentrange

  def incidentrange(self, val):
    """
    List
    
    regular range in incident angle in degrees, one of step; min max or min max step. Default min is 0 and step is 10.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{incidentrange} must be a list, not {val}")
    self._incidentrange = val
    return self

  def get_rayparamrad(self):
    return self._rayparamrad

  def rayparamrad(self, val):
    """
    List
    
    ray parameter from the source in s/rad, up or down is determined by the phase
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamrad} must be a list, not {val}")
    self._rayparamrad = val
    return self

  def get_rayparamdeg(self):
    return self._rayparamdeg

  def rayparamdeg(self, val):
    """
    List
    
    ray parameter from the source in s/deg, up or down is determined by the phase
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamdeg} must be a list, not {val}")
    self._rayparamdeg = val
    return self

  def get_rayparamkm(self):
    return self._rayparamkm

  def rayparamkm(self, val):
    """
    List
    
    ray parameter from the source in s/km, up or down is determined by the phase
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamkm} must be a list, not {val}")
    self._rayparamkm = val
    return self

  def get_rayparamidx(self):
    return self._rayparamidx

  def rayparamidx(self, val):
    """
    List
    
    ray parameter from the source as index into model sampling, up or down is determined by the phase
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamidx} must be a list, not {val}")
    self._rayparamidx = val
    return self

  def get_allindex(self):
    return self._allindex

  def allindex(self, val):
    """
    Boolean
    
    all arrivals at sampling of model
    """
    self._allindex = val
    return self

  def get_station(self):
    return self._station

  def station(self, val):
    """
    List
    
    station latitude and longitude. Creates a distance if event is also given.
    Also known as --sta and --station in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{station} must be a list, not {val}")
    self._station = val
    return self

  def get_event(self):
    return self._event

  def event(self, val):
    """
    List
    
    event latitude and longitude.  Creates a distance if station is also given.
    Also known as --evt and --event in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{event} must be a list, not {val}")
    self._event = val
    return self

  def get_az(self):
    return self._az

  def az(self, val):
    """
    Double
    
    azimuth in degrees, source to receiver
    """
    self._az = val
    return self

  def get_baz(self):
    return self._baz

  def baz(self, val):
    """
    Double
    
    backazimuth in degrees, receiver to source
    """
    self._baz = val
    return self

  def get_geodetic(self):
    return self._geodetic

  def geodetic(self, val):
    """
    Boolean
    
    use geodetic latitude for distance calculations, which implies an ellipticity. Default is spherical. Note this only affects calculation of distance from lat/lon pairs, all travel time calculations are done in a purely spherical model.
    """
    self._geodetic = val
    return self

  def get_geodeticflattening(self):
    return self._geodeticflattening

  def geodeticflattening(self, val):
    """
    Double
    
    Inverse Elliptical flattening for distance calculations when --geodetic, defaults to WGS84 ~ 298.257. The distance calculation uses 1/x.
    """
    self._geodeticflattening = val
    return self

  def get_eid(self):
    return self._eid

  def eid(self, val):
    """
    List
    
    event id, like us7000pn9s, for lookup via USGS fdsn event web service. Creates a distance if station is also given.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{eid} must be a list, not {val}")
    self._eid = val
    return self

  def get_sid(self):
    return self._sid

  def sid(self, val):
    """
    List
    
    station id, like CO.HAW or FDSN:CO_HAW, for lookup via fedcat web service. Creates a distance if event is also given.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sid} must be a list, not {val}")
    self._sid = val
    return self

  def get_quakeml(self):
    return self._quakeml

  def quakeml(self, val):
    """
    String
    
    QuakeML file to load for earthquake origins to use
    Also known as --qml and --quakeml in command line.
    """
    self._quakeml = val
    return self

  def get_staxml(self):
    return self._staxml

  def staxml(self, val):
    """
    String
    
    StationXML file to extract station latitudes and longitudes from
    """
    self._staxml = val
    return self

  def get_onlyrayp(self):
    return self._onlyrayp

  def onlyrayp(self, val):
    """
    Boolean
    
    only output the ray parameter
    Also known as --rayp and --onlyrayp in command line.
    """
    self._onlyrayp = val
    return self

  def get_onlytime(self):
    return self._onlytime

  def onlytime(self, val):
    """
    Boolean
    
    only output travel time
    Also known as --time and --onlytime in command line.
    """
    self._onlytime = val
    return self

  def get_onlyfirst(self):
    return self._onlyfirst

  def onlyfirst(self, val):
    """
    Boolean
    
    only output the first arrival for each phase, no triplications
    Also known as --first and --onlyfirst in command line.
    """
    self._onlyfirst = val
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

  def get_amp(self):
    return self._amp

  def amp(self, val):
    """
    Boolean
    
    show amplitude factor for each phase
    """
    self._amp = val
    return self

  def get_rel(self):
    return self._rel

  def rel(self, val):
    """
    List
    
    times relative to the first of the given phases
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rel} must be a list, not {val}")
    self._rel = val
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
    if len(self._degree) > 0:
      params["degree"] = self._degree
    if len(self._degreerange) > 0:
      params["degreerange"] = self._degreerange
    if len(self._kilometer) > 0:
      params["kilometer"] = self._kilometer
    if len(self._kilometerrange) > 0:
      params["kilometerrange"] = self._kilometerrange
    if len(self._exactdegree) > 0:
      params["exactdegree"] = self._exactdegree
    if len(self._exactdegreerange) > 0:
      params["exactdegreerange"] = self._exactdegreerange
    if len(self._exactkilometer) > 0:
      params["exactkilometer"] = self._exactkilometer
    if len(self._exactkilometerrange) > 0:
      params["exactkilometerrange"] = self._exactkilometerrange
    if len(self._takeoff) > 0:
      params["takeoff"] = self._takeoff
    if len(self._takeoffrange) > 0:
      params["takeoffrange"] = self._takeoffrange
    if len(self._incident) > 0:
      params["incident"] = self._incident
    if len(self._incidentrange) > 0:
      params["incidentrange"] = self._incidentrange
    if len(self._rayparamrad) > 0:
      params["rayparamrad"] = self._rayparamrad
    if len(self._rayparamdeg) > 0:
      params["rayparamdeg"] = self._rayparamdeg
    if len(self._rayparamkm) > 0:
      params["rayparamkm"] = self._rayparamkm
    if len(self._rayparamidx) > 0:
      params["rayparamidx"] = self._rayparamidx
    if self._allindex is not None:
      params["allindex"] = self._allindex
    if len(self._station) > 0:
      params["station"] = self._station
    if len(self._event) > 0:
      params["event"] = self._event
    if self._az is not None:
      params["az"] = self._az
    if self._baz is not None:
      params["baz"] = self._baz
    if self._geodetic is not None:
      params["geodetic"] = self._geodetic
    if self._geodeticflattening is not None:
      params["geodeticflattening"] = self._geodeticflattening
    if len(self._eid) > 0:
      params["eid"] = self._eid
    if len(self._sid) > 0:
      params["sid"] = self._sid
    if self._quakeml is not None:
      params["quakeml"] = self._quakeml
    if self._staxml is not None:
      params["staxml"] = self._staxml
    if self._onlyrayp is not None:
      params["onlyrayp"] = self._onlyrayp
    if self._onlytime is not None:
      params["onlytime"] = self._onlytime
    if self._onlyfirst is not None:
      params["onlyfirst"] = self._onlyfirst
    if self._attenuationfreq is not None:
      params["attenuationfreq"] = self._attenuationfreq
    if self._numattenuationfreq is not None:
      params["numattenuationfreq"] = self._numattenuationfreq
    if len(self._strikediprake) > 0:
      params["strikediprake"] = self._strikediprake
    if self._mw is not None:
      params["mw"] = self._mw
    if self._amp is not None:
      params["amp"] = self._amp
    if len(self._rel) > 0:
      params["rel"] = self._rel
    return params

