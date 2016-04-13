from rinse.message import SoapMessage
from request import SoapNoAuthRequest


class SysQueryRequest(SoapNoAuthRequest):
    def __init__(self, url, key, country, sysvar):
        super().__init__(url, key, country)
        self._sysvar = sysvar

    def _create_message(self):
        msg = SoapMessage()
        s = msg.elementmaker("s", self._url)

        msg.body = s.DoQuerySysStatusRequest(
            s.sysvar(self._sysvar),
            s.countryId(self._country),
            s.webapiKey(self._key)
        )

        return msg
