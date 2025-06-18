class VersionQuery:
  def __init__(self):
    self.toolname= "version"


  def calc(self, taupServer):
    params = self.create_params()
    return taupServer.queryJson(params, self.toolname)



  def create_params(self):
    """
    Create dict of params suitible for passing to requests query call.
    """
    params = {
      "format": "json",
    }
    return params

