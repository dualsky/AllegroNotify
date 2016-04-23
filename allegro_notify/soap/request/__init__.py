

class SoapRequest:
    @staticmethod
    def get_response_class():
        raise NotImplementedError

    def _create_message(self, ns):
        raise NotImplementedError


class SoapAuthRequest(SoapRequest):
    def __init__(self, session):
        self._session = session


class SoapNoAuthRequest(SoapRequest):
    def __init__(self, key, country):
        self._key = key
        self._country = country


from soap.request.item_list import *
from soap.request.login import *
from soap.request.sys_query import *
