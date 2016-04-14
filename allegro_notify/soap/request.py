from rinse.client import SoapClient
from soap.response import Response


class SoapRequest:
    def send(self, url, ns=None):
        if ns is None:
            ns = url
        client = SoapClient(url)
        msg = self._create_message(ns)
        return client(msg, build_response=Response)

    def _create_message(self, ns):
        raise NotImplementedError


class SoapAuthRequest(SoapRequest):
    def __init__(self, session):
        self._session = session


class SoapNoAuthRequest(SoapRequest):
    def __init__(self, key, country):
        self._key = key
        self._country = country
