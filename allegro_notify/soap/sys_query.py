from rinse.message import SoapMessage
from soap.request import SoapNoAuthRequest


class SysQueryRequest(SoapNoAuthRequest):
    def __init__(self, key, country, sysvar):
        super().__init__(key, country)
        self._sysvar = sysvar

    def _create_message(self, url):
        msg = SoapMessage()
        s = msg.elementmaker("s", url)

        msg.body = s.DoQuerySysStatusRequest(
            s.sysvar(self._sysvar),
            s.countryId(self._country),
            s.webapiKey(self._key)
        )

        return msg
