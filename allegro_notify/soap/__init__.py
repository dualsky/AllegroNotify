import rinse.client


class SoapClient:
  def __init__(self, url, ns=None):
    self._url = url
    self._ns = ns

  def send(self, req):
    if self._ns is None:
        self._ns = self._url
    client = rinse.client.SoapClient(self._url)
    msg = req._create_message(self._ns)
    return client(msg, build_response=req.get_response_class())


class SoapFault(Exception):
    def __init__(self, code, desc):
        super().__init__(code)
        self._desc = desc

    @property
    def desc(self):
        return self._desc


from soap.request import *
from soap.response import *
