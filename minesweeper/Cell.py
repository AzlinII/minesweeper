class Cell:
    def __init__(self, sign = "?"):
        self._sign = sign

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, value):
        self._sign = value

