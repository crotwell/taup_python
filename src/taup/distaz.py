
# autogenerated from picocli command line arguments in TauP
# For The TauP Toolkit, version: 3.0.2-SNAPSHOT_2025-07-14T122228

from .dataclass import DistazResult

class DistazQuery:
  def __init__(self):
    self.toolname= "distaz"

    self._az=None
    self._baz=None
    self._degree=[]
    self._degreerange=[]
    self._event=[]
    self._geodetic=None
    self._geodeticflattening=None
    self._kilometer=[]
    self._kilometerrange=[]
    self._model=None
    self._radius=None
    self._station=[]

  def calc(self, taupServer):
    """
    Sends all params to the server, returns the result parsed from JSON into dataclasses.
    """
    params = self.create_params()
    return DistazResult.from_json(self.calcJson(taupServer))

  def calcJson(self, taupServer):
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
    params.deg( value )
    and
    params.deg( [ value ] )
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
    params.deg( value )
    and
    params.deg( [ value ] )
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
    params.degree( value )
    and
    params.degree( [ value ] )
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
    params.degree( value )
    and
    params.degree( [ value ] )
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
    step or min,max or min,max,step

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
    step or min,max or min,max,step

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

  def get_km(self):
    """
    returns current value of kilometer as a List
    """
    return self._kilometer

  def km(self, val):
    """
    Sets the kilometer parameter, of type List of Double
    If a single Double is passed in, it is automatically wrapped in a list. So
    params.km( value )
    and
    params.km( [ value ] )
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
    params.km( value )
    and
    params.km( [ value ] )
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
    params.kilometer( value )
    and
    params.kilometer( [ value ] )
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
    params.kilometer( value )
    and
    params.kilometer( [ value ] )
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
    step or min,max or min,max,step

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
    step or min,max or min,max,step

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

    use velocity model "modelName" for radius, used when distance given in km.

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

    use velocity model "modelName" for radius, used when distance given in km.

    Known as --model in command line.

    :param val: value to set model to
    """
    self._model = val
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

    Known as --radius in command line.

    :param val: value to set radius to
    """
    self._radius = val
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
    if self._model is not None:
      params["model"] = self._model
    if self._radius is not None:
      params["radius"] = self._radius
    if len(self._station) > 0:
      params["station"] = self._station
    return params

