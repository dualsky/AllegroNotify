from rinse.message import SoapMessage
from soap.request import SoapNoAuthRequest


class LoginRequset(SoapNoAuthRequest):
    def __init__(self, key, country, login, pwd_hash, version):
        super().__init__(key, country)
        self._login = login
        self._pwd_hash = pwd_hash
        self._version = version

    def _create_message(self, ns):
        msg = SoapMessage()
        s = msg.elementmaker("s", ns)

        msg.body = s.DoLoginEncRequest(
            s.userLogin(self._login),
            s.userHashPassword(self._pwd_hash),
            s.countryCode(self._country),
            s.webapiKey(self._key),
            s.localVersion(self._version))

        return msg
