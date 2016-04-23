from rinse import NS_MAP
from rinse.util import safe_parse_string
from soap import SoapFault


class SoapResponse():
    def __init__(self, response):
        self._response = response

        # Parse response
        try:
            self._doc = safe_parse_string(response.content)
            self._body = self._doc.xpath(
                "/soapenv:Envelope/soapenv:Body", namespaces=NS_MAP)[0]
        except:
            raise SoapFault("ResponseParseError", "Cannot parse response")

        self._fault = self._body.find("soapenv:Fault", NS_MAP)
        if self._fault is not None:
            raise SoapFault(self._fault.find("faultcode").text,
                            self._fault.find("faultstring").text)

        # Get and set Allegro API namespaces
        self._ns = NS_MAP.copy()
        for i, v in enumerate(self._doc.nsmap.values()):
            if v != NS_MAP["soapenv"]:
                self._ns["ns{}".format(i)] = v


from soap.response.item_list import *
