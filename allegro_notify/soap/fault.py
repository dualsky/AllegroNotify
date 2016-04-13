class SoapFault(Exception):
    def __init__(self, code, string):
        self._code = code
        self._string = string

    @property
    def code(self):
        return self._code

    @property
    def string(self):
        return self._string
