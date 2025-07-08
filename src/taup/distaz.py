class DistazQuery:
  def __init__(self):
    self.toolname= "distaz"

    self._az=None
    self._baz=None
    self._degree=[]
    self._degreerange=[]
    self._eid=[]
    self._event=[]
    self._geodetic=None
    self._geodeticflattening=None
    self._kilometer=[]
    self._kilometerrange=[]
    self._quakeml=None
    self._radius=None
    self._sid=[]
    self._station=[]
    self._staxml=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_az(self):
    """
    returns current value of az as a Double
    """
    return self._az

  def az(self, val):
    """
    Sets the az parameter, of type Double    
    azimuth in degrees, source to receiver

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

    :param val: value to set degreerange to
    """
    self._degreerange.append(val)
    return self

  def get_eid(self):
    """
    returns current value of eid as a List
    """
    return self._eid

  def eid(self, val):
    """
    Sets the eid parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.eid( value )
    and 
    .xeid( [ value ] )
    are equivalent. 
    
    event id, like us7000pn9s, for lookup via USGS fdsn event web service. Creates a distance if station is also given.

    :param val: value to set eid to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._eid = val
    return self


  def andEid(self, val):
    """
    Sets the eid parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.eid( value )
    and 
    .xeid( [ value ] )
    are equivalent. 
    
    event id, like us7000pn9s, for lookup via USGS fdsn event web service. Creates a distance if station is also given.

    :param val: value to set eid to
    """
    self._eid.append(val)
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
    Also known as --event in command line.

    :param val: value to set event to
    """
    self._event = [lat, lon]
    return self

  def andEvt(self, lat, lon):
    """
    Sets the event parameter, of type List of Double
    
    event latitude and longitude.  Creates a distance if station is also given.
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

    :param val: value to set event to
    """
    self._event = [lat, lon]
    return self

  def andEvent(self, lat, lon):
    """
    Sets the event parameter, of type List of Double
    
    event latitude and longitude.  Creates a distance if station is also given.

    :param val: value to set event to
    """
    self._event += [lat, lon]
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

    :param val: value to set geodeticflattening to
    """
    self._geodeticflattening = val
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

    :param val: value to set kilometerrange to
    """
    self._kilometerrange.append(val)
    return self

  def get_qml(self):
    """
    returns current value of quakeml as a String
    """
    return self._quakeml

  def qml(self, val):
    """
    Sets the quakeml parameter, of type String    
    QuakeML file to load for earthquake origins to use
    Also known as --quakeml in command line.

    :param val: value to set quakeml to
    """
    self._quakeml = val
    return self

  def get_quakeml(self):
    """
    returns current value of quakeml as a String
    """
    return self._quakeml

  def quakeml(self, val):
    """
    Sets the quakeml parameter, of type String    
    QuakeML file to load for earthquake origins to use

    :param val: value to set quakeml to
    """
    self._quakeml = val
    return self

  def get_radius(self):
    """
    returns current value of radius as a Double
    """
    return self._radius

  def radius(self, val):
    """
    Sets the radius parameter, of type Double    
    radius of earth in km, used when distance given in km

    :param val: value to set radius to
    """
    self._radius = val
    return self

  def get_sid(self):
    """
    returns current value of sid as a List
    """
    return self._sid

  def sid(self, val):
    """
    Sets the sid parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.sid( value )
    and 
    .xsid( [ value ] )
    are equivalent. 
    
    station id, like CO.HAW or FDSN:CO_HAW, for lookup via fedcat web service. Creates a distance if event is also given.

    :param val: value to set sid to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._sid = val
    return self


  def andSid(self, val):
    """
    Sets the sid parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.sid( value )
    and 
    .xsid( [ value ] )
    are equivalent. 
    
    station id, like CO.HAW or FDSN:CO_HAW, for lookup via fedcat web service. Creates a distance if event is also given.

    :param val: value to set sid to
    """
    self._sid.append(val)
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
    Also known as --station in command line.

    :param val: value to set station to
    """
    self._station = [lat, lon]
    return self

  def andSta(self, lat, lon):
    """
    Sets the station parameter, of type List of Double
    
    station latitude and longitude. Creates a distance if event is also given.
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

    :param val: value to set station to
    """
    self._station = [lat, lon]
    return self

  def andStation(self, lat, lon):
    """
    Sets the station parameter, of type List of Double
    
    station latitude and longitude. Creates a distance if event is also given.

    :param val: value to set station to
    """
    self._station += [lat, lon]
    return self

  def get_staxml(self):
    """
    returns current value of staxml as a String
    """
    return self._staxml

  def staxml(self, val):
    """
    Sets the staxml parameter, of type String    
    StationXML file to extract station latitudes and longitudes from

    :param val: value to set staxml to
    """
    self._staxml = val
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._az is not None:
      params["az"] = self._az
    if self._baz is not None:
      params["baz"] = self._baz
    if len(self._degree) > 0:
      params["degree"] = self._degree
    if len(self._degreerange) > 0:
      params["degreerange"] = self._degreerange
    if len(self._eid) > 0:
      params["eid"] = self._eid
    if len(self._event) > 0:
      params["event"] = self._event
    if self._geodetic is not None:
      params["geodetic"] = self._geodetic
    if self._geodeticflattening is not None:
      params["geodeticflattening"] = self._geodeticflattening
    if len(self._kilometer) > 0:
      params["kilometer"] = self._kilometer
    if len(self._kilometerrange) > 0:
      params["kilometerrange"] = self._kilometerrange
    if self._quakeml is not None:
      params["quakeml"] = self._quakeml
    if self._radius is not None:
      params["radius"] = self._radius
    if len(self._sid) > 0:
      params["sid"] = self._sid
    if len(self._station) > 0:
      params["station"] = self._station
    if self._staxml is not None:
      params["staxml"] = self._staxml
    return params

