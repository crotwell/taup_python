class WavefrontQuery:
  def __init__(self):
    self.toolname= "wavefront"

    self._color=None
    self._degminmax=None
    self._depthminmax=None
    self._legend=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._model=None
    self._negdist=None
    self._onlynameddiscon=None
    self._phase=[]
    self._phasefile=[]
    self._receiverdepth=[]
    self._scatter=[]
    self._sourcedepth=[]
    self._timefiles=None
    self._timestep=None
    self._xaxis=None
    self._yaxis=None

  def calc(self, taupServer):
    """
    Sends all params to the server, returns the result parsed from JSON.
    """
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)


  def calcGmt(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of gmt.
    """
    params = self.create_params()
    return taupServer.queryGmt(params, self.toolname)


  def calcHtml(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of html.
    """
    params = self.create_params()
    return taupServer.queryHtml(params, self.toolname)


  def calcSvg(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of svg.
    """
    params = self.create_params()
    return taupServer.querySvg(params, self.toolname)


  def calcText(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of text.
    """
    params = self.create_params()
    return taupServer.queryText(params, self.toolname)


  def get_color(self):
    """
    returns current value of color as a edu.sc.seis.TauP.cmdline.args.ColorType
    """
    return self._color

  def color(self, val):
    """
    Sets the color parameter, of type edu.sc.seis.TauP.cmdline.args.ColorType    
    style of coloring for paths and wavefronts, one of: auto, wavetype, phase, none

    :param val: value to set color to
    """
    self._color = val
    return self

  def get_degminmax(self):
    """
    returns current value of degminmax as a [D
    """
    return self._degminmax

  def degminmax(self, val):
    """
    Sets the degminmax parameter, of type [D    
    min and max distance in degrees for plotting

    :param val: value to set degminmax to
    """
    self._degminmax = val
    return self

  def get_depthminmax(self):
    """
    returns current value of depthminmax as a [D
    """
    return self._depthminmax

  def depthminmax(self, val):
    """
    Sets the depthminmax parameter, of type [D    
    min and max depth, km,  for plotting

    :param val: value to set depthminmax to
    """
    self._depthminmax = val
    return self

  def get_legend(self):
    """
    returns current value of legend as a Boolean
    """
    return self._legend

  def legend(self, val):
    """
    Sets the legend parameter, of type Boolean    
    create a legend

    :param val: value to set legend to
    """
    self._legend = val
    return self

  def get_mapwidth(self):
    """
    returns current value of mapwidth as a Float
    """
    return self._mapwidth

  def mapwidth(self, val):
    """
    Sets the mapwidth parameter, of type Float    
    plot width in units from --mapwidthunit.

    :param val: value to set mapwidth to
    """
    self._mapwidth = val
    return self

  def get_mapwidthunit(self):
    """
    returns current value of mapwidthunit as a String
    """
    return self._mapwidthunit

  def mapwidthunit(self, val):
    """
    Sets the mapwidthunit parameter, of type String    
    plot width unit, i for inch, c for cm or p for px.

    :param val: value to set mapwidthunit to
    """
    self._mapwidthunit = val
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

    :param val: value to set model to
    """
    self._model = val
    return self

  def get_negdist(self):
    """
    returns current value of negdist as a Boolean
    """
    return self._negdist

  def negdist(self, val):
    """
    Sets the negdist parameter, of type Boolean    
    outputs negative distance as well so wavefronts are in both halves.

    :param val: value to set negdist to
    """
    self._negdist = val
    return self

  def get_onlynameddiscon(self):
    """
    returns current value of onlynameddiscon as a Boolean
    """
    return self._onlynameddiscon

  def onlynameddiscon(self, val):
    """
    Sets the onlynameddiscon parameter, of type Boolean    
    only draw circles on the plot for named discontinuities like moho, cmb, iocb but not 410

    :param val: value to set onlynameddiscon to
    """
    self._onlynameddiscon = val
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
    Also known as --phase in command line.

    :param val: value to set phase to
    """
    self._phase.append(val)
    return self

  def get_phasefile(self):
    """
    returns current value of phasefile as a List
    """
    return self._phasefile

  def phasefile(self, val):
    """
    Sets the phasefile parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phasefile( value )
    and 
    .xphasefile( [ value ] )
    are equivalent. 
    
    read list of phase names from file

    :param val: value to set phasefile to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._phasefile = val
    return self


  def andPhasefile(self, val):
    """
    Sets the phasefile parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So 
    x.phasefile( value )
    and 
    .xphasefile( [ value ] )
    are equivalent. 
    
    read list of phase names from file

    :param val: value to set phasefile to
    """
    self._phasefile.append(val)
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

    :param val: value to set receiverdepth to
    """
    self._receiverdepth.append(val)
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
    Also known as --sourcedepth in command line.

    :param val: value to set sourcedepth to
    """
    self._sourcedepth.append(val)
    return self

  def get_timefiles(self):
    """
    returns current value of timefiles as a Boolean
    """
    return self._timefiles

  def timefiles(self, val):
    """
    Sets the timefiles parameter, of type Boolean    
    outputs each time into a separate file within the gmt script.

    :param val: value to set timefiles to
    """
    self._timefiles = val
    return self

  def get_timestep(self):
    """
    returns current value of timestep as a Float
    """
    return self._timestep

  def timestep(self, val):
    """
    Sets the timestep parameter, of type Float    
    steps in time (seconds) for output, default is 100

    :param val: value to set timestep to
    """
    self._timestep = val
    return self

  def get_xaxis(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.DistanceAxisType
    """
    return self._xaxis

  def xaxis(self, val):
    """
    Sets the xaxis parameter, of type edu.sc.seis.TauP.DistanceAxisType    
    x axis type, the depth/radius axis, one of degree, radian, kilometer
    No effect for SVG output.

    :param val: value to set xaxis to
    """
    self._xaxis = val
    return self

  def get_yaxis(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.DepthAxisType
    """
    return self._yaxis

  def yaxis(self, val):
    """
    Sets the yaxis parameter, of type edu.sc.seis.TauP.DepthAxisType    
    y axis type, the depth/radius axis, one of depth, radius
    No effect for SVG output.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._color is not None:
      params["color"] = self._color
    if self._degminmax is not None:
      params["degminmax"] = self._degminmax
    if self._depthminmax is not None:
      params["depthminmax"] = self._depthminmax
    if self._legend is not None:
      params["legend"] = self._legend
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if self._model is not None:
      params["model"] = self._model
    if self._negdist is not None:
      params["negdist"] = self._negdist
    if self._onlynameddiscon is not None:
      params["onlynameddiscon"] = self._onlynameddiscon
    if len(self._phase) > 0:
      params["phase"] = self._phase
    if len(self._phasefile) > 0:
      params["phasefile"] = self._phasefile
    if len(self._receiverdepth) > 0:
      params["receiverdepth"] = self._receiverdepth
    if len(self._scatter) > 0:
      params["scatter"] = self._scatter
    if len(self._sourcedepth) > 0:
      params["sourcedepth"] = self._sourcedepth
    if self._timefiles is not None:
      params["timefiles"] = self._timefiles
    if self._timestep is not None:
      params["timestep"] = self._timestep
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    return params

