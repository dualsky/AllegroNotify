from rinse.client import SoapClient
from utils.soap_response import Response


class SoapRequest:
    def __init__(self, url):
        self._url = url

    def send(self):
        client = SoapClient(self._url)
        msg = self._create_message()
        return client(msg, build_response=Response)

    def _create_message(self):
        raise NotImplementedError


class SoapAuthRequest(SoapRequest):
    def __init__(self, url, session):
        super().__init__(url)
        self._session = session


class SoapNoAuthRequest(SoapRequest):
    def __init__(self, url, key, country):
        super().__init__(url)
        self._key = key
        self._country = country
