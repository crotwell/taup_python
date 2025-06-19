class DistazQuery:
  def __init__(self):
    self.toolname= "distaz"

    self._station=[]
    self._event=[]
    self._az=None
    self._baz=None
    self._eid=[]
    self._sid=[]
    self._quakeml=None
    self._staxml=None
    self._geodetic=None
    self._geodeticflattening=None
    self._degree=[]
    self._degreerange=[]
    self._kilometer=[]
    self._kilometerrange=[]
    self._radius=None

  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def get_sta(self):
    return self._station

  def sta(self, val):
    """
    List of Double

    
    station latitude and longitude. Creates a distance if event is also given.
    Also known as --station in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sta} must be a list, not {val}")
    self._station = val
    return self

  def get_station(self):
    return self._station

  def station(self, val):
    """
    List of Double

    
    station latitude and longitude. Creates a distance if event is also given.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{station} must be a list, not {val}")
    self._station = val
    return self

  def get_evt(self):
    return self._event

  def evt(self, val):
    """
    List of Double

    
    event latitude and longitude.  Creates a distance if station is also given.
    Also known as --event in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{evt} must be a list, not {val}")
    self._event = val
    return self

  def get_event(self):
    return self._event

  def event(self, val):
    """
    List of Double

    
    event latitude and longitude.  Creates a distance if station is also given.
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

  def get_eid(self):
    return self._eid

  def eid(self, val):
    """
    List of String

    
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
    List of String

    
    station id, like CO.HAW or FDSN:CO_HAW, for lookup via fedcat web service. Creates a distance if event is also given.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sid} must be a list, not {val}")
    self._sid = val
    return self

  def get_qml(self):
    return self._quakeml

  def qml(self, val):
    """
    String
    
    QuakeML file to load for earthquake origins to use
    Also known as --quakeml in command line.
    """
    self._quakeml = val
    return self

  def get_quakeml(self):
    return self._quakeml

  def quakeml(self, val):
    """
    String
    
    QuakeML file to load for earthquake origins to use
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

  def get_deg(self):
    return self._degree

  def deg(self, val):
    """
    List of Double

    
    distance in degrees
    Also known as --degree in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{deg} must be a list, not {val}")
    self._degree = val
    return self

  def get_degree(self):
    return self._degree

  def degree(self, val):
    """
    List of Double

    
    distance in degrees
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degree} must be a list, not {val}")
    self._degree = val
    return self

  def get_degreerange(self):
    return self._degreerange

  def degreerange(self, val):
    """
    List of Double

    
    regular distance range in degrees, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degreerange} must be a list, not {val}")
    self._degreerange = val
    return self

  def get_km(self):
    return self._kilometer

  def km(self, val):
    """
    List of Double

    
    distance in kilometers along surface.
    Also known as --kilometer in command line.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{km} must be a list, not {val}")
    self._kilometer = val
    return self

  def get_kilometer(self):
    return self._kilometer

  def kilometer(self, val):
    """
    List of Double

    
    distance in kilometers along surface.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{kilometer} must be a list, not {val}")
    self._kilometer = val
    return self

  def get_kilometerrange(self):
    return self._kilometerrange

  def kilometerrange(self, val):
    """
    List of Double

    
    regular distance range in kilometers, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    """
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{kilometerrange} must be a list, not {val}")
    self._kilometerrange = val
    return self

  def get_radius(self):
    return self._radius

  def radius(self, val):
    """
    Double
    
    radius of earth in km, used when distance given in km
    """
    self._radius = val
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if len(self._station) > 0:
      params["station"] = self._station
    if len(self._event) > 0:
      params["event"] = self._event
    if self._az is not None:
      params["az"] = self._az
    if self._baz is not None:
      params["baz"] = self._baz
    if len(self._eid) > 0:
      params["eid"] = self._eid
    if len(self._sid) > 0:
      params["sid"] = self._sid
    if self._quakeml is not None:
      params["quakeml"] = self._quakeml
    if self._staxml is not None:
      params["staxml"] = self._staxml
    if self._geodetic is not None:
      params["geodetic"] = self._geodetic
    if self._geodeticflattening is not None:
      params["geodeticflattening"] = self._geodeticflattening
    if len(self._degree) > 0:
      params["degree"] = self._degree
    if len(self._degreerange) > 0:
      params["degreerange"] = self._degreerange
    if len(self._kilometer) > 0:
      params["kilometer"] = self._kilometer
    if len(self._kilometerrange) > 0:
      params["kilometerrange"] = self._kilometerrange
    if self._radius is not None:
      params["radius"] = self._radius
    return params

