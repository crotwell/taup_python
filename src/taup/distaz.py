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


  @property
  def station(self):
    """
    List
    
    station latitude and longitude. Creates a distance if event is also given.
    Also known as --sta and --station in command line.
    """
    return self._station

  @station.setter
  def station(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{station} must be a list, not {val}")
    self._station = val

  @property
  def event(self):
    """
    List
    
    event latitude and longitude.  Creates a distance if station is also given.
    Also known as --evt and --event in command line.
    """
    return self._event

  @event.setter
  def event(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{event} must be a list, not {val}")
    self._event = val

  @property
  def az(self):
    """
    Double
    
    azimuth in degrees, source to receiver
    """
    return self._az

  @az.setter
  def az(self, val):
    self._az = val

  @property
  def baz(self):
    """
    Double
    
    backazimuth in degrees, receiver to source
    """
    return self._baz

  @baz.setter
  def baz(self, val):
    self._baz = val

  @property
  def eid(self):
    """
    List
    
    event id, like us7000pn9s, for lookup via USGS fdsn event web service. Creates a distance if station is also given.
    """
    return self._eid

  @eid.setter
  def eid(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{eid} must be a list, not {val}")
    self._eid = val

  @property
  def sid(self):
    """
    List
    
    station id, like CO.HAW or FDSN:CO_HAW, for lookup via fedcat web service. Creates a distance if event is also given.
    """
    return self._sid

  @sid.setter
  def sid(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{sid} must be a list, not {val}")
    self._sid = val

  @property
  def quakeml(self):
    """
    String
    
    QuakeML file to load for earthquake origins to use
    Also known as --qml and --quakeml in command line.
    """
    return self._quakeml

  @quakeml.setter
  def quakeml(self, val):
    self._quakeml = val

  @property
  def staxml(self):
    """
    String
    
    StationXML file to extract station latitudes and longitudes from
    """
    return self._staxml

  @staxml.setter
  def staxml(self, val):
    self._staxml = val

  @property
  def geodetic(self):
    """
    Boolean
    
    use geodetic latitude for distance calculations, which implies an ellipticity. Default is spherical. Note this only affects calculation of distance from lat/lon pairs, all travel time calculations are done in a purely spherical model.
    """
    return self._geodetic

  @geodetic.setter
  def geodetic(self, val):
    self._geodetic = val

  @property
  def geodeticflattening(self):
    """
    Double
    
    Inverse Elliptical flattening for distance calculations when --geodetic, defaults to WGS84 ~ 298.257. The distance calculation uses 1/x.
    """
    return self._geodeticflattening

  @geodeticflattening.setter
  def geodeticflattening(self, val):
    self._geodeticflattening = val

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

  @property
  def degreerange(self):
    """
    List
    
    regular distance range in degrees, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    """
    return self._degreerange

  @degreerange.setter
  def degreerange(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{degreerange} must be a list, not {val}")
    self._degreerange = val

  @property
  def kilometer(self):
    """
    List
    
    distance in kilometers along surface.
    Also known as --km and --kilometer in command line.
    """
    return self._kilometer

  @kilometer.setter
  def kilometer(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{kilometer} must be a list, not {val}")
    self._kilometer = val

  @property
  def kilometerrange(self):
    """
    List
    
    regular distance range in kilometers, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    """
    return self._kilometerrange

  @kilometerrange.setter
  def kilometerrange(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{kilometerrange} must be a list, not {val}")
    self._kilometerrange = val

  @property
  def radius(self):
    """
    Double
    
    radius of earth in km, used when distance given in km
    """
    return self._radius

  @radius.setter
  def radius(self, val):
    self._radius = val


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

