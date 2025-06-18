class WavefrontQuery:
  def __init__(self):
    self.toolname= "wavefront"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phasefile=[]
    self._phase=[]
    self._color=None
    self._legend=None
    self._onlynameddiscon=None
    self._yaxis=None
    self._xaxis=None
    self._degminmax=None
    self._depthminmax=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._timestep=None
    self._timefiles=None
    self._negdist=None

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
  def onlynameddiscon(self):
    """
    Boolean
    
    only draw circles on the plot for named discontinuities like moho, cmb, iocb but not 410
    """
    return self._onlynameddiscon

  @onlynameddiscon.setter
  def onlynameddiscon(self, val):
    self._onlynameddiscon = val

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
  def timestep(self):
    """
    Float
    
    steps in time (seconds) for output, default is 100
    """
    return self._timestep

  @timestep.setter
  def timestep(self, val):
    self._timestep = val

  @property
  def timefiles(self):
    """
    Boolean
    
    outputs each time into a separate file within the gmt script.
    """
    return self._timefiles

  @timefiles.setter
  def timefiles(self, val):
    self._timefiles = val

  @property
  def negdist(self):
    """
    Boolean
    
    outputs negative distance as well so wavefronts are in both halves.
    """
    return self._negdist

  @negdist.setter
  def negdist(self, val):
    self._negdist = val


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
    if self._color is not None:
      params["color"] = self._color
    if self._legend is not None:
      params["legend"] = self._legend
    if self._onlynameddiscon is not None:
      params["onlynameddiscon"] = self._onlynameddiscon
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    if self._degminmax is not None:
      params["degminmax"] = self._degminmax
    if self._depthminmax is not None:
      params["depthminmax"] = self._depthminmax
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._timestep is not None:
      params["timestep"] = self._timestep
    if self._timefiles is not None:
      params["timefiles"] = self._timefiles
    if self._negdist is not None:
      params["negdist"] = self._negdist
    return params

