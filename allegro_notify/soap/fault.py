class SoapFault(Exception):
    def __init__(self, code, desc):
        super().__init__(code)
        self._desc = desc

    @property
    def desc(self):
        return self._desc
