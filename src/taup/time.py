class TimeQuery:
  def __init__(self):
    self.toolname= "time"

    self._allindex=None
    self._amp=None
    self._attenuationfreq=None
    self._az=None
    self._baz=None
    self._degree=[]
    self._degreerange=[]
    self._event=[]
    self._exactdegree=[]
    self._exactdegreerange=[]
    self._exactkilometer=[]
    self._exactkilometerrange=[]
    self._geodetic=None
    self._geodeticflattening=None
    self._incident=[]
    self._incidentrange=[]
    self._kilometer=[]
    self._kilometerrange=[]
    self._model=None
    self._mw=None
    self._numattenuationfreq=None
    self._onlyfirst=None
    self._onlyrayp=None
    self._onlytime=None
    self._phase=[]
    self._rayparamdeg=[]
    self._rayparamidx=[]
    self._rayparamkm=[]
    self._rayparamrad=[]
    self._receiverdepth=[]
    self._rel=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._station=[]
    self._strikediprake=[]
    self._takeoff=[]
    self._takeoffrange=[]

  def calc(self, taupServer):
    """
    Sends all params to the server, returns the result parsed from JSON.
    """
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def calcHtml(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of html.
    """
    params = self.create_params()
    return taupServer.queryHtml(params, self.toolname)


  def calcText(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of text.
    """
    params = self.create_params()
    return taupServer.queryText(params, self.toolname)


  def get_allindex(self):
    """
    returns current value of allindex as a Boolean
    """
    return self._allindex

  def allindex(self, val):
    """
    Sets the allindex parameter, of type Boolean    
    all arrivals at sampling of model
    Known as --allindex in command line.

    :param val: value to set allindex to
    """
    self._allindex = val
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
    Known as --amp in command line.

    :param val: value to set amp to
    """
    self._amp = val
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
    azimuth in degrees, source to receiver
    Known as --az in command line.

    :param val: value to set az to
    """
    self._az = val
    return self

  def get_baz(self):
    """
    returns current value of baz as a Double
    """
    return self._baz

  def baz(self, val):
    """
    Sets the baz parameter, of type Double    
    backazimuth in degrees, receiver to source
    Known as --baz in command line.

    :param val: value to set baz to
    """
    self._baz = val
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
    Known as --deg in command line.
    Also known as --degree in command line.

    :param val: value to set degree to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._degree = val
    return self


  def andDeg(self, val):
    """
    Sets the degree parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.deg( value )
    and 
    .xdeg( [ value ] )
    are equivalent. 
    
    distance in degrees
    Known as --deg in command line.
    Also known as --degree in command line.

    :param val: value to set degree to
    """
    self._degree.append(val)
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
    Known as --degree in command line.

    :param val: value to set degree to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._degree = val
    return self


  def andDegree(self, val):
    """
    Sets the degree parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.degree( value )
    and 
    .xdegree( [ value ] )
    are equivalent. 
    
    distance in degrees
    Known as --degree in command line.

    :param val: value to set degree to
    """
    self._degree.append(val)
    return self

  def get_degreerange(self):
    """
    returns current value of degreerange as a List
    """
    return self._degreerange

  def degreerange(self, val):
    """
    Sets the degreerange parameter, of type List of Double
    
    regular distance range in degrees, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    Known as --degreerange in command line.

    :param val: value to set degreerange to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"degreerange() requires a list, not {val}")
    self._degreerange = val
    return self


  def andDegreerange(self, val):
    """
    Sets the degreerange parameter, of type List of Double
    
    regular distance range in degrees, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    Known as --degreerange in command line.

    :param val: value to set degreerange to
    """
    self._degreerange.append(val)
    return self

  def get_evt(self):
    """
    returns current value of event as a List
    """
    return self._event

  def evt(self, lat, lon):
    """
    Sets the event parameter, of type List of Double
    
    event latitude and longitude.  Creates a distance if station is also given.
    Known as --evt in command line.
    Also known as --event in command line.

    :param val: value to set event to
    """
    self._event = [lat, lon]
    return self

  def andEvt(self, lat, lon):
    """
    Sets the event parameter, of type List of Double
    
    event latitude and longitude.  Creates a distance if station is also given.
    Known as --evt in command line.
    Also known as --event in command line.

    :param val: value to set event to
    """
    self._event += [lat, lon]
    return self

  def get_event(self):
    """
    returns current value of event as a List
    """
    return self._event

  def event(self, lat, lon):
    """
    Sets the event parameter, of type List of Double
    
    event latitude and longitude.  Creates a distance if station is also given.
    Known as --event in command line.

    :param val: value to set event to
    """
    self._event = [lat, lon]
    return self

  def andEvent(self, lat, lon):
    """
    Sets the event parameter, of type List of Double
    
    event latitude and longitude.  Creates a distance if station is also given.
    Known as --event in command line.

    :param val: value to set event to
    """
    self._event += [lat, lon]
    return self

  def get_exactdegree(self):
    """
    returns current value of exactdegree as a List
    """
    return self._exactdegree

  def exactdegree(self, val):
    """
    Sets the exactdegree parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.exactdegree( value )
    and 
    .xexactdegree( [ value ] )
    are equivalent. 
    
    exact distance traveled in degrees, not 360-d
    Known as --exactdegree in command line.

    :param val: value to set exactdegree to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._exactdegree = val
    return self


  def andExactdegree(self, val):
    """
    Sets the exactdegree parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.exactdegree( value )
    and 
    .xexactdegree( [ value ] )
    are equivalent. 
    
    exact distance traveled in degrees, not 360-d
    Known as --exactdegree in command line.

    :param val: value to set exactdegree to
    """
    self._exactdegree.append(val)
    return self

  def get_exactdegreerange(self):
    """
    returns current value of exactdegreerange as a List
    """
    return self._exactdegreerange

  def exactdegreerange(self, val):
    """
    Sets the exactdegreerange parameter, of type List of Double
    
    regular distance range in exact degrees, not 360-deg, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    Known as --exactdegreerange in command line.

    :param val: value to set exactdegreerange to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"exactdegreerange() requires a list, not {val}")
    self._exactdegreerange = val
    return self


  def andExactdegreerange(self, val):
    """
    Sets the exactdegreerange parameter, of type List of Double
    
    regular distance range in exact degrees, not 360-deg, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    Known as --exactdegreerange in command line.

    :param val: value to set exactdegreerange to
    """
    self._exactdegreerange.append(val)
    return self

  def get_exactkilometer(self):
    """
    returns current value of exactkilometer as a List
    """
    return self._exactkilometer

  def exactkilometer(self, val):
    """
    Sets the exactkilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.exactkilometer( value )
    and 
    .xexactkilometer( [ value ] )
    are equivalent. 
    
    exact distance traveled in kilometers, not 360-k
    Known as --exactkilometer in command line.

    :param val: value to set exactkilometer to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._exactkilometer = val
    return self


  def andExactkilometer(self, val):
    """
    Sets the exactkilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.exactkilometer( value )
    and 
    .xexactkilometer( [ value ] )
    are equivalent. 
    
    exact distance traveled in kilometers, not 360-k
    Known as --exactkilometer in command line.

    :param val: value to set exactkilometer to
    """
    self._exactkilometer.append(val)
    return self

  def get_exactkilometerrange(self):
    """
    returns current value of exactkilometerrange as a List
    """
    return self._exactkilometerrange

  def exactkilometerrange(self, val):
    """
    Sets the exactkilometerrange parameter, of type List of Double
    
    regular distance range in kilometers, not 360-k, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    Known as --exactkilometerrange in command line.

    :param val: value to set exactkilometerrange to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"exactkilometerrange() requires a list, not {val}")
    self._exactkilometerrange = val
    return self


  def andExactkilometerrange(self, val):
    """
    Sets the exactkilometerrange parameter, of type List of Double
    
    regular distance range in kilometers, not 360-k, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    Known as --exactkilometerrange in command line.

    :param val: value to set exactkilometerrange to
    """
    self._exactkilometerrange.append(val)
    return self

  def get_geodetic(self):
    """
    returns current value of geodetic as a Boolean
    """
    return self._geodetic

  def geodetic(self, val):
    """
    Sets the geodetic parameter, of type Boolean    
    use geodetic latitude for distance calculations, which implies an ellipticity. Default is spherical. Note this only affects calculation of distance from lat/lon pairs, all travel time calculations are done in a purely spherical model.
    Known as --geodetic in command line.

    :param val: value to set geodetic to
    """
    self._geodetic = val
    return self

  def get_geodeticflattening(self):
    """
    returns current value of geodeticflattening as a Double
    """
    return self._geodeticflattening

  def geodeticflattening(self, val):
    """
    Sets the geodeticflattening parameter, of type Double    
    Inverse Elliptical flattening for distance calculations when --geodetic, defaults to WGS84 ~ 298.257. The distance calculation uses 1/x.
    Known as --geodeticflattening in command line.

    :param val: value to set geodeticflattening to
    """
    self._geodeticflattening = val
    return self

  def get_incident(self):
    """
    returns current value of incident as a List
    """
    return self._incident

  def incident(self, val):
    """
    Sets the incident parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.incident( value )
    and 
    .xincident( [ value ] )
    are equivalent. 
    
    incident angle in degrees at the receiver, zero is down, 90 horizontal, 180 is up.
    Known as --incident in command line.

    :param val: value to set incident to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._incident = val
    return self


  def andIncident(self, val):
    """
    Sets the incident parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.incident( value )
    and 
    .xincident( [ value ] )
    are equivalent. 
    
    incident angle in degrees at the receiver, zero is down, 90 horizontal, 180 is up.
    Known as --incident in command line.

    :param val: value to set incident to
    """
    self._incident.append(val)
    return self

  def get_incidentrange(self):
    """
    returns current value of incidentrange as a List
    """
    return self._incidentrange

  def incidentrange(self, val):
    """
    Sets the incidentrange parameter, of type List of Double
    
    regular range in incident angle in degrees, one of step; min max or min max step. Default min is 0 and step is 10.
    Known as --incidentrange in command line.

    :param val: value to set incidentrange to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"incidentrange() requires a list, not {val}")
    self._incidentrange = val
    return self


  def andIncidentrange(self, val):
    """
    Sets the incidentrange parameter, of type List of Double
    
    regular range in incident angle in degrees, one of step; min max or min max step. Default min is 0 and step is 10.
    Known as --incidentrange in command line.

    :param val: value to set incidentrange to
    """
    self._incidentrange.append(val)
    return self

  def get_km(self):
    """
    returns current value of kilometer as a List
    """
    return self._kilometer

  def km(self, val):
    """
    Sets the kilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.km( value )
    and 
    .xkm( [ value ] )
    are equivalent. 
    
    distance in kilometers along surface.
    Known as --km in command line.
    Also known as --kilometer in command line.

    :param val: value to set kilometer to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._kilometer = val
    return self


  def andKm(self, val):
    """
    Sets the kilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.km( value )
    and 
    .xkm( [ value ] )
    are equivalent. 
    
    distance in kilometers along surface.
    Known as --km in command line.
    Also known as --kilometer in command line.

    :param val: value to set kilometer to
    """
    self._kilometer.append(val)
    return self

  def get_kilometer(self):
    """
    returns current value of kilometer as a List
    """
    return self._kilometer

  def kilometer(self, val):
    """
    Sets the kilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.kilometer( value )
    and 
    .xkilometer( [ value ] )
    are equivalent. 
    
    distance in kilometers along surface.
    Known as --kilometer in command line.

    :param val: value to set kilometer to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._kilometer = val
    return self


  def andKilometer(self, val):
    """
    Sets the kilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.kilometer( value )
    and 
    .xkilometer( [ value ] )
    are equivalent. 
    
    distance in kilometers along surface.
    Known as --kilometer in command line.

    :param val: value to set kilometer to
    """
    self._kilometer.append(val)
    return self

  def get_kilometerrange(self):
    """
    returns current value of kilometerrange as a List
    """
    return self._kilometerrange

  def kilometerrange(self, val):
    """
    Sets the kilometerrange parameter, of type List of Double
    
    regular distance range in kilometers, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    Known as --kilometerrange in command line.

    :param val: value to set kilometerrange to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"kilometerrange() requires a list, not {val}")
    self._kilometerrange = val
    return self


  def andKilometerrange(self, val):
    """
    Sets the kilometerrange parameter, of type List of Double
    
    regular distance range in kilometers, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    Known as --kilometerrange in command line.

    :param val: value to set kilometerrange to
    """
    self._kilometerrange.append(val)
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

  def get_first(self):
    """
    returns current value of onlyfirst as a Boolean
    """
    return self._onlyfirst

  def first(self, val):
    """
    Sets the onlyfirst parameter, of type Boolean    
    only output the first arrival for each phase, no triplications
    Known as --first in command line.
    Also known as --onlyfirst in command line.

    :param val: value to set onlyfirst to
    """
    self._onlyfirst = val
    return self

  def get_onlyfirst(self):
    """
    returns current value of onlyfirst as a Boolean
    """
    return self._onlyfirst

  def onlyfirst(self, val):
    """
    Sets the onlyfirst parameter, of type Boolean    
    only output the first arrival for each phase, no triplications
    Known as --onlyfirst in command line.

    :param val: value to set onlyfirst to
    """
    self._onlyfirst = val
    return self

  def get_rayp(self):
    """
    returns current value of onlyrayp as a Boolean
    """
    return self._onlyrayp

  def rayp(self, val):
    """
    Sets the onlyrayp parameter, of type Boolean    
    only output the ray parameter
    Known as --rayp in command line.
    Also known as --onlyrayp in command line.

    :param val: value to set onlyrayp to
    """
    self._onlyrayp = val
    return self

  def get_onlyrayp(self):
    """
    returns current value of onlyrayp as a Boolean
    """
    return self._onlyrayp

  def onlyrayp(self, val):
    """
    Sets the onlyrayp parameter, of type Boolean    
    only output the ray parameter
    Known as --onlyrayp in command line.

    :param val: value to set onlyrayp to
    """
    self._onlyrayp = val
    return self

  def get_time(self):
    """
    returns current value of onlytime as a Boolean
    """
    return self._onlytime

  def time(self, val):
    """
    Sets the onlytime parameter, of type Boolean    
    only output travel time
    Known as --time in command line.
    Also known as --onlytime in command line.

    :param val: value to set onlytime to
    """
    self._onlytime = val
    return self

  def get_onlytime(self):
    """
    returns current value of onlytime as a Boolean
    """
    return self._onlytime

  def onlytime(self, val):
    """
    Sets the onlytime parameter, of type Boolean    
    only output travel time
    Known as --onlytime in command line.

    :param val: value to set onlytime to
    """
    self._onlytime = val
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

  def get_rayparamdeg(self):
    """
    returns current value of rayparamdeg as a List
    """
    return self._rayparamdeg

  def rayparamdeg(self, val):
    """
    Sets the rayparamdeg parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.rayparamdeg( value )
    and 
    .xrayparamdeg( [ value ] )
    are equivalent. 
    
    ray parameter from the source in s/deg, up or down is determined by the phase
    Known as --rayparamdeg in command line.

    :param val: value to set rayparamdeg to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._rayparamdeg = val
    return self


  def andRayparamdeg(self, val):
    """
    Sets the rayparamdeg parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.rayparamdeg( value )
    and 
    .xrayparamdeg( [ value ] )
    are equivalent. 
    
    ray parameter from the source in s/deg, up or down is determined by the phase
    Known as --rayparamdeg in command line.

    :param val: value to set rayparamdeg to
    """
    self._rayparamdeg.append(val)
    return self

  def get_rayparamidx(self):
    """
    returns current value of rayparamidx as a List
    """
    return self._rayparamidx

  def rayparamidx(self, val):
    """
    Sets the rayparamidx parameter, of type List of java.lang.Integer
    If a single java.lang.Integer is passed in, it is automatically wrapped in a list. So 
    x.rayparamidx( value )
    and 
    .xrayparamidx( [ value ] )
    are equivalent. 
    
    ray parameter from the source as index into model sampling, up or down is determined by the phase
    Known as --rayparamidx in command line.

    :param val: value to set rayparamidx to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._rayparamidx = val
    return self


  def andRayparamidx(self, val):
    """
    Sets the rayparamidx parameter, of type List of java.lang.Integer
    If a single java.lang.Integer is passed in, it is automatically wrapped in a list. So 
    x.rayparamidx( value )
    and 
    .xrayparamidx( [ value ] )
    are equivalent. 
    
    ray parameter from the source as index into model sampling, up or down is determined by the phase
    Known as --rayparamidx in command line.

    :param val: value to set rayparamidx to
    """
    self._rayparamidx.append(val)
    return self

  def get_rayparamkm(self):
    """
    returns current value of rayparamkm as a List
    """
    return self._rayparamkm

  def rayparamkm(self, val):
    """
    Sets the rayparamkm parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.rayparamkm( value )
    and 
    .xrayparamkm( [ value ] )
    are equivalent. 
    
    ray parameter from the source in s/km, up or down is determined by the phase
    Known as --rayparamkm in command line.

    :param val: value to set rayparamkm to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._rayparamkm = val
    return self


  def andRayparamkm(self, val):
    """
    Sets the rayparamkm parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.rayparamkm( value )
    and 
    .xrayparamkm( [ value ] )
    are equivalent. 
    
    ray parameter from the source in s/km, up or down is determined by the phase
    Known as --rayparamkm in command line.

    :param val: value to set rayparamkm to
    """
    self._rayparamkm.append(val)
    return self

  def get_rayparamrad(self):
    """
    returns current value of rayparamrad as a List
    """
    return self._rayparamrad

  def rayparamrad(self, val):
    """
    Sets the rayparamrad parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.rayparamrad( value )
    and 
    .xrayparamrad( [ value ] )
    are equivalent. 
    
    ray parameter from the source in s/rad, up or down is determined by the phase
    Known as --rayparamrad in command line.

    :param val: value to set rayparamrad to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._rayparamrad = val
    return self


  def andRayparamrad(self, val):
    """
    Sets the rayparamrad parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.rayparamrad( value )
    and 
    .xrayparamrad( [ value ] )
    are equivalent. 
    
    ray parameter from the source in s/rad, up or down is determined by the phase
    Known as --rayparamrad in command line.

    :param val: value to set rayparamrad to
    """
    self._rayparamrad.append(val)
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

  def get_rel(self):
    """
    returns current value of rel as a List
    """
    return self._rel

  def rel(self, val):
    """
    Sets the rel parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.rel( value )
    and 
    .xrel( [ value ] )
    are equivalent. 
    
    times relative to the first of the given phases
    Known as --rel in command line.

    :param val: value to set rel to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._rel = val
    return self


  def andRel(self, val):
    """
    Sets the rel parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.rel( value )
    and 
    .xrel( [ value ] )
    are equivalent. 
    
    times relative to the first of the given phases
    Known as --rel in command line.

    :param val: value to set rel to
    """
    self._rel.append(val)
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

  def get_sta(self):
    """
    returns current value of station as a List
    """
    return self._station

  def sta(self, lat, lon):
    """
    Sets the station parameter, of type List of Double
    
    station latitude and longitude. Creates a distance if event is also given.
    Known as --sta in command line.
    Also known as --station in command line.

    :param val: value to set station to
    """
    self._station = [lat, lon]
    return self

  def andSta(self, lat, lon):
    """
    Sets the station parameter, of type List of Double
    
    station latitude and longitude. Creates a distance if event is also given.
    Known as --sta in command line.
    Also known as --station in command line.

    :param val: value to set station to
    """
    self._station += [lat, lon]
    return self

  def get_station(self):
    """
    returns current value of station as a List
    """
    return self._station

  def station(self, lat, lon):
    """
    Sets the station parameter, of type List of Double
    
    station latitude and longitude. Creates a distance if event is also given.
    Known as --station in command line.

    :param val: value to set station to
    """
    self._station = [lat, lon]
    return self

  def andStation(self, lat, lon):
    """
    Sets the station parameter, of type List of Double
    
    station latitude and longitude. Creates a distance if event is also given.
    Known as --station in command line.

    :param val: value to set station to
    """
    self._station += [lat, lon]
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

  def get_takeoff(self):
    """
    returns current value of takeoff as a List
    """
    return self._takeoff

  def takeoff(self, val):
    """
    Sets the takeoff parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.takeoff( value )
    and 
    .xtakeoff( [ value ] )
    are equivalent. 
    
    takeoff angle in degrees from the source, zero is down, 90 horizontal, 180 is up.
    Known as --takeoff in command line.

    :param val: value to set takeoff to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._takeoff = val
    return self


  def andTakeoff(self, val):
    """
    Sets the takeoff parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So 
    x.takeoff( value )
    and 
    .xtakeoff( [ value ] )
    are equivalent. 
    
    takeoff angle in degrees from the source, zero is down, 90 horizontal, 180 is up.
    Known as --takeoff in command line.

    :param val: value to set takeoff to
    """
    self._takeoff.append(val)
    return self

  def get_takeoffrange(self):
    """
    returns current value of takeoffrange as a List
    """
    return self._takeoffrange

  def takeoffrange(self, val):
    """
    Sets the takeoffrange parameter, of type List of Double
    
    regular range in takeoff angle in degrees, one of step; min,max or min,max,step. Default min is 0 and step is 10.
    Known as --takeoffrange in command line.

    :param val: value to set takeoffrange to
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"takeoffrange() requires a list, not {val}")
    self._takeoffrange = val
    return self


  def andTakeoffrange(self, val):
    """
    Sets the takeoffrange parameter, of type List of Double
    
    regular range in takeoff angle in degrees, one of step; min,max or min,max,step. Default min is 0 and step is 10.
    Known as --takeoffrange in command line.

    :param val: value to set takeoffrange to
    """
    self._takeoffrange.append(val)
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._allindex is not None:
      params["allindex"] = self._allindex
    if self._amp is not None:
      params["amp"] = self._amp
    if self._attenuationfreq is not None:
      params["attenuationfreq"] = self._attenuationfreq
    if self._az is not None:
      params["az"] = self._az
    if self._baz is not None:
      params["baz"] = self._baz
    if len(self._degree) > 0:
      params["degree"] = self._degree
    if len(self._degreerange) > 0:
      params["degreerange"] = self._degreerange
    if len(self._event) > 0:
      params["event"] = self._event
    if len(self._exactdegree) > 0:
      params["exactdegree"] = self._exactdegree
    if len(self._exactdegreerange) > 0:
      params["exactdegreerange"] = self._exactdegreerange
    if len(self._exactkilometer) > 0:
      params["exactkilometer"] = self._exactkilometer
    if len(self._exactkilometerrange) > 0:
      params["exactkilometerrange"] = self._exactkilometerrange
    if self._geodetic is not None:
      params["geodetic"] = self._geodetic
    if self._geodeticflattening is not None:
      params["geodeticflattening"] = self._geodeticflattening
    if len(self._incident) > 0:
      params["incident"] = self._incident
    if len(self._incidentrange) > 0:
      params["incidentrange"] = self._incidentrange
    if len(self._kilometer) > 0:
      params["kilometer"] = self._kilometer
    if len(self._kilometerrange) > 0:
      params["kilometerrange"] = self._kilometerrange
    if self._model is not None:
      params["model"] = self._model
    if self._mw is not None:
      params["mw"] = self._mw
    if self._numattenuationfreq is not None:
      params["numattenuationfreq"] = self._numattenuationfreq
    if self._onlyfirst is not None:
      params["onlyfirst"] = self._onlyfirst
    if self._onlyrayp is not None:
      params["onlyrayp"] = self._onlyrayp
    if self._onlytime is not None:
      params["onlytime"] = self._onlytime
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._rayparamdeg) > 0:
      params["rayparamdeg"] = self._rayparamdeg
    if len(self._rayparamidx) > 0:
      params["rayparamidx"] = self._rayparamidx
    if len(self._rayparamkm) > 0:
      params["rayparamkm"] = self._rayparamkm
    if len(self._rayparamrad) > 0:
      params["rayparamrad"] = self._rayparamrad
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._rel) > 0:
      params["rel"] = self._rel
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._sourcedepth) > 0:
      params["sourcedepth"] = self._sourcedepth
    if len(self._station) > 0:
      params["station"] = self._station
    if len(self._strikediprake) > 0:
      params["strikediprake"] = self._strikediprake
    if len(self._takeoff) > 0:
      params["takeoff"] = self._takeoff
    if len(self._takeoffrange) > 0:
      params["takeoffrange"] = self._takeoffrange
    return params

