from rinse import NS_MAP
from rinse.util import safe_parse_string
from soap.fault import SoapFault


class Response(object):
    def __init__(self, response):
        """Response init."""
        self._response = response
        # parse response
        self._doc = safe_parse_string(response.content)
        self._body = self._doc.xpath(
            "/soapenv:Envelope/soapenv:Body", namespaces=NS_MAP,
        )[0]
        self._fault = self._body.find("soapenv:Fault", NS_MAP)
        if self._fault is not None:
            raise SoapFault(self._fault.find("faultcode").text,
                            self._fault.find("faultstring").text)

    def __str__(self):
        """String representation of Response is the HTTP body content."""
        return self._response.content.decode("utf-8")
