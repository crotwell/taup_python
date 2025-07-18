
# autogenerated from picocli command line arguments in TauP
# For The TauP Toolkit, version: 3.0.2-SNAPSHOT_2025-07-14T122228

class VelplotQuery:
  def __init__(self):
    self.toolname= "velplot"

    self._legend=None
    self._mapwidth=None
    self._mapwidthunit=None
    self._model=[]
    self._xaxis=None
    self._xminmax=None
    self._yaxis=None
    self._yminmax=None

  def calcJson(self, taupServer):
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


  def calcCsv(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of csv.
    """
    params = self.create_params()
    return taupServer.queryCsv(params, self.toolname)


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


  def calcNameddiscon(self, taupServer):
    """
    Sends all params to the server, returns the result as a text version of nameddiscon.
    """
    params = self.create_params()
    return taupServer.queryNameddiscon(params, self.toolname)


  def get_legend(self):
    """
    returns current value of legend as a Boolean
    """
    return self._legend

  def legend(self, val):
    """
    Sets the legend parameter, of type Boolean

    create a legend

    Known as --legend in command line.

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

    Known as --mapwidth in command line.

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

    Known as --mapwidthunit in command line.

    :param val: value to set mapwidthunit to
    """
    self._mapwidthunit = val
    return self

  def get_mod(self):
    """
    returns current value of model as a List
    """
    return self._model

  def mod(self, val):
    """
    Sets the model parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So
    params.mod( value )
    and
    params.mod( [ value ] )
    are equivalent.

    use velocity model "modelname" for calculations, format is guessed.

    Known as --mod in command line.
    Also known as --model in command line.

    :param val: value to set model to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._model = val
    return self


  def andMod(self, val):
    """
    Sets the model parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So
    params.mod( value )
    and
    params.mod( [ value ] )
    are equivalent.

    use velocity model "modelname" for calculations, format is guessed.

    Known as --mod in command line.
    Also known as --model in command line.

    :param val: value to set model to
    """
    self._model.append(val)
    return self

  def get_model(self):
    """
    returns current value of model as a List
    """
    return self._model

  def model(self, val):
    """
    Sets the model parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So
    params.model( value )
    and
    params.model( [ value ] )
    are equivalent.

    use velocity model "modelname" for calculations, format is guessed.

    Known as --model in command line.

    :param val: value to set model to
    """
    if not hasattr(val, "__getitem__"):
      val = [ val ]
    self._model = val
    return self


  def andModel(self, val):
    """
    Sets the model parameter, of type List of String
    If a single String is passed in, it is automatically wrapped in a list. So
    params.model( value )
    and
    params.model( [ value ] )
    are equivalent.

    use velocity model "modelname" for calculations, format is guessed.

    Known as --model in command line.

    :param val: value to set model to
    """
    self._model.append(val)
    return self

  def get_x(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._xaxis

  def x(self, val):
    """
    Sets the xaxis parameter, a choice of one of:
     depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus

    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.

    Known as -x in command line.
    Also known as --xaxis in command line.

    :param val: value to set xaxis to
    """
    self._xaxis = val
    return self

  def get_xaxis(self):
    """
    returns current value of xaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._xaxis

  def xaxis(self, val):
    """
    Sets the xaxis parameter, a choice of one of:
     depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus

    X axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is velocity.

    Known as --xaxis in command line.

    :param val: value to set xaxis to
    """
    self._xaxis = val
    return self

  def get_xminmax(self):
    """
    returns current value of xminmax as a [D
    """
    return self._xminmax

  def xminmax(self, val):
    """
    Sets the xminmax parameter, of type [D

    min and max x axis for plotting

    Known as --xminmax in command line.

    :param val: value to set xminmax to
    """
    self._xminmax = val
    return self

  def get_y(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._yaxis

  def y(self, val):
    """
    Sets the yaxis parameter, a choice of one of:
     depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus

    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.

    Known as -y in command line.
    Also known as --yaxis in command line.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self

  def get_yaxis(self):
    """
    returns current value of yaxis as a edu.sc.seis.TauP.ModelAxisType
    """
    return self._yaxis

  def yaxis(self, val):
    """
    Sets the yaxis parameter, a choice of one of:
     depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus

    Y axis data type, one of depth, radius, velocity, Vp, Vs, slownessdeg, slownessdeg_p, slownessdeg_s, slownessrad, slownessrad_p, slownessrad_s, density, velocity_density, Qp, Qs, Q, vpvs, vpdensity, vsdensity, poisson, shearmodulus, lambda, bulkmodulus, youngsmodulus
    Default is depth.

    Known as --yaxis in command line.

    :param val: value to set yaxis to
    """
    self._yaxis = val
    return self

  def get_yminmax(self):
    """
    returns current value of yminmax as a [D
    """
    return self._yminmax

  def yminmax(self, val):
    """
    Sets the yminmax parameter, of type [D

    min and max y axis for plotting

    Known as --yminmax in command line.

    :param val: value to set yminmax to
    """
    self._yminmax = val
    return self


  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    if self._legend is not None:
      params["legend"] = self._legend
    if self._mapwidth is not None:
      params["mapwidth"] = self._mapwidth
    if self._mapwidthunit is not None:
      params["mapwidthunit"] = self._mapwidthunit
    if len(self._model) > 0:
      params["model"] = self._model
    if self._xaxis is not None:
      params["xaxis"] = self._xaxis
    if self._xminmax is not None:
      params["xminmax"] = self._xminmax
    if self._yaxis is not None:
      params["yaxis"] = self._yaxis
    if self._yminmax is not None:
      params["yminmax"] = self._yminmax
    return params

