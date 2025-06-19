class WavefrontQuery:
  def __init__(self):
    self.toolname= "wavefront"

    self._model=None
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._phase=[]
    self._phasefile=[]
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

  def get_color(self):
    return self._color

  def color(self, val):
    """
    edu.sc.seis.TauP.cmdline.args.ColorType
    
    style of coloring for paths and wavefronts, one of: auto, wavetype, phase, none
    """
    self._color = val
    return self

  def get_legend(self):
    return self._legend

  def legend(self, val):
    """
    Boolean
    
    create a legend
    """
    self._legend = val
    return self

  def get_onlynameddiscon(self):
    return self._onlynameddiscon

  def onlynameddiscon(self, val):
    """
    Boolean
    
    only draw circles on the plot for named discontinuities like moho, cmb, iocb but not 410
    """
    self._onlynameddiscon = val
    return self

  def get_yaxis(self):
    return self._yaxis

  def yaxis(self, val):
    """
    edu.sc.seis.TauP.DepthAxisType
    
    y axis type, the depth/radius axis, one of depth, radius
    No effect for SVG output.
    """
    self._yaxis = val
    return self

  def get_xaxis(self):
    return self._xaxis

  def xaxis(self, val):
    """
    edu.sc.seis.TauP.DistanceAxisType
    
    x axis type, the depth/radius axis, one of degree, radian, kilometer
    No effect for SVG output.
    """
    self._xaxis = val
    return self

  def get_degminmax(self):
    return self._degminmax

  def degminmax(self, val):
    """
    [D
    
    min and max distance in degrees for plotting
    """
    self._degminmax = val
    return self

  def get_depthminmax(self):
    return self._depthminmax

  def depthminmax(self, val):
    """
    [D
    
    min and max depth, km,  for plotting
    """
    self._depthminmax = val
    return self

  def get_mapwidth(self):
    return self._mapwidth

  def mapwidth(self, val):
    """
    Float
    
    plot width in units from --mapwidthunit.
    """
    self._mapwidth = val
    return self

  def get_mapwidthunit(self):
    return self._mapwidthunit

  def mapwidthunit(self, val):
    """
    String
    
    plot width unit, i for inch, c for cm or p for px.
    """
    self._mapwidthunit = val
    return self

  def get_timestep(self):
    return self._timestep

  def timestep(self, val):
    """
    Float
    
    steps in time (seconds) for output, default is 100
    """
    self._timestep = val
    return self

  def get_timefiles(self):
    return self._timefiles

  def timefiles(self, val):
    """
    Boolean
    
    outputs each time into a separate file within the gmt script.
    """
    self._timefiles = val
    return self

  def get_negdist(self):
    return self._negdist

  def negdist(self, val):
    """
    Boolean
    
    outputs negative distance as well so wavefronts are in both halves.
    """
    self._negdist = val
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

