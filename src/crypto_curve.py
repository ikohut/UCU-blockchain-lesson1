class CryptoCurve:
    def __init__(self, a=0, b=7, p=131):
        self.a = a
        self.b = b
        self.p = p

    def generate_params(self):
        pass

    def get_params(self):
        return (self.a, self.b, self.p)
