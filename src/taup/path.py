class PathQuery:
  def __init__(self):
    self.toolname= "path"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phasefile=[]
    self._phase=[]
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
    self._color=None
    self._legend=None
    self._label=None
    self._yaxis=None
    self._xaxis=None
    self._degminmax=None
    self._depthminmax=None
    self._onlynameddiscon=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._withtime=None
    self._maxpathinc=None

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
  def exactdegree(self):
    """
    List
    
    exact distance traveled in degrees, not 360-d
    """
    return self._exactdegree

  @exactdegree.setter
  def exactdegree(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactdegree} must be a list, not {val}")
    self._exactdegree = val

  @property
  def exactdegreerange(self):
    """
    List
    
    regular distance range in exact degrees, not 360-deg, one of step; min max or min max step. Default min is 0, max is 180 and step is 10.
    """
    return self._exactdegreerange

  @exactdegreerange.setter
  def exactdegreerange(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactdegreerange} must be a list, not {val}")
    self._exactdegreerange = val

  @property
  def exactkilometer(self):
    """
    List
    
    exact distance traveled in kilometers, not 360-k
    """
    return self._exactkilometer

  @exactkilometer.setter
  def exactkilometer(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactkilometer} must be a list, not {val}")
    self._exactkilometer = val

  @property
  def exactkilometerrange(self):
    """
    List
    
    regular distance range in kilometers, not 360-k, one of step; min max or min max step. Default min is 0, max is 1000 and step is 100.
    """
    return self._exactkilometerrange

  @exactkilometerrange.setter
  def exactkilometerrange(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{exactkilometerrange} must be a list, not {val}")
    self._exactkilometerrange = val

  @property
  def takeoff(self):
    """
    List
    
    takeoff angle in degrees from the source, zero is down, 90 horizontal, 180 is up.
    """
    return self._takeoff

  @takeoff.setter
  def takeoff(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{takeoff} must be a list, not {val}")
    self._takeoff = val

  @property
  def takeoffrange(self):
    """
    List
    
    regular range in takeoff angle in degrees, one of step; min,max or min,max,step. Default min is 0 and step is 10.
    """
    return self._takeoffrange

  @takeoffrange.setter
  def takeoffrange(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{takeoffrange} must be a list, not {val}")
    self._takeoffrange = val

  @property
  def incident(self):
    """
    List
    
    incident angle in degrees at the receiver, zero is down, 90 horizontal, 180 is up.
    """
    return self._incident

  @incident.setter
  def incident(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{incident} must be a list, not {val}")
    self._incident = val

  @property
  def incidentrange(self):
    """
    List
    
    regular range in incident angle in degrees, one of step; min max or min max step. Default min is 0 and step is 10.
    """
    return self._incidentrange

  @incidentrange.setter
  def incidentrange(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{incidentrange} must be a list, not {val}")
    self._incidentrange = val

  @property
  def rayparamrad(self):
    """
    List
    
    ray parameter from the source in s/rad, up or down is determined by the phase
    """
    return self._rayparamrad

  @rayparamrad.setter
  def rayparamrad(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamrad} must be a list, not {val}")
    self._rayparamrad = val

  @property
  def rayparamdeg(self):
    """
    List
    
    ray parameter from the source in s/deg, up or down is determined by the phase
    """
    return self._rayparamdeg

  @rayparamdeg.setter
  def rayparamdeg(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamdeg} must be a list, not {val}")
    self._rayparamdeg = val

  @property
  def rayparamkm(self):
    """
    List
    
    ray parameter from the source in s/km, up or down is determined by the phase
    """
    return self._rayparamkm

  @rayparamkm.setter
  def rayparamkm(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamkm} must be a list, not {val}")
    self._rayparamkm = val

  @property
  def rayparamidx(self):
    """
    List
    
    ray parameter from the source as index into model sampling, up or down is determined by the phase
    """
    return self._rayparamidx

  @rayparamidx.setter
  def rayparamidx(self, val):
    if not hasattr(val, "__getitem__"):
      raise Exception(f"{rayparamidx} must be a list, not {val}")
    self._rayparamidx = val

  @property
  def allindex(self):
    """
    Boolean
    
    all arrivals at sampling of model
    """
    return self._allindex

  @allindex.setter
  def allindex(self, val):
    self._allindex = val

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
  def color(self):
    """
    edu.sc.seis.TauP.cmdline.args.ColorType
    
    style of coloring for paths and wavefronts, one of: auto, wavetype, phase, none
    """
    return self._color

  @color.setter
  def color(self, val):
    self._color = val

  @property
  def legend(self):
    """
    Boolean
    
    create a legend
    """
    return self._legend

  @legend.setter
  def legend(self, val):
    self._legend = val

  @property
  def label(self):
    """
    Boolean
    
    label with phase name
    """
    return self._label

  @label.setter
  def label(self, val):
    self._label = val

  @property
  def yaxis(self):
    """
    edu.sc.seis.TauP.DepthAxisType
    
    y axis type, the depth/radius axis, one of depth, radius
    No effect for SVG output.
    """
    return self._yaxis

  @yaxis.setter
  def yaxis(self, val):
    self._yaxis = val

  @property
  def xaxis(self):
    """
    edu.sc.seis.TauP.DistanceAxisType
    
    x axis type, the depth/radius axis, one of degree, radian, kilometer
    No effect for SVG output.
    """
    return self._xaxis

  @xaxis.setter
  def xaxis(self, val):
    self._xaxis = val

  @property
  def degminmax(self):
    """
    [D
    
    min and max distance in degrees for plotting
    """
    return self._degminmax

  @degminmax.setter
  def degminmax(self, val):
    self._degminmax = val

  @property
  def depthminmax(self):
    """
    [D
    
    min and max depth, km,  for plotting
    """
    return self._depthminmax

  @depthminmax.setter
  def depthminmax(self, val):
    self._depthminmax = val

  @property
  def onlynameddiscon(self):
    """
    Boolean
    
    only draw circles on the plot for named discontinuities like moho, cmb, iocb
    """
    return self._onlynameddiscon

  @onlynameddiscon.setter
  def onlynameddiscon(self, val):
    self._onlynameddiscon = val

  @property
  def mapwidth(self):
    """
    Float
    
    plot width in units from --mapwidthunit.
    """
    return self._mapwidth

  @mapwidth.setter
  def mapwidth(self, val):
    self._mapwidth = val

  @property
  def mapwidthunit(self):
    """
    String
    
    plot width unit, i for inch, c for cm or p for px.
    """
    return self._mapwidthunit

  @mapwidthunit.setter
  def mapwidthunit(self, val):
    self._mapwidthunit = val

  @property
  def withtime(self):
    """
    Boolean
    
    include time for each path point, no effect for SVG.
    """
    return self._withtime

  @withtime.setter
  def withtime(self, val):
    self._withtime = val

  @property
  def maxpathinc(self):
    """
    Double
    
    Maximum distance increment in degrees between path points, avoid visible segmentation in plots
    """
    return self._maxpathinc

  @maxpathinc.setter
  def maxpathinc(self, val):
    self._maxpathinc = val


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
    if self._color is not None:
      params["color"] = self._color
    if self._legend is not None:
      params["legend"] = self._legend
    if self._label is not None:
      params["label"] = self._label
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    if self._degminmax is not None:
      params["degminmax"] = self._degminmax
    if self._depthminmax is not None:
      params["depthminmax"] = self._depthminmax
    if self._onlynameddiscon is not None:
      params["onlynameddiscon"] = self._onlynameddiscon
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._withtime is not None:
      params["withtime"] = self._withtime
    if self._maxpathinc is not None:
      params["maxpathinc"] = self._maxpathinc
    return params

