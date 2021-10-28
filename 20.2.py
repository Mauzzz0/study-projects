class Bureaucracy():
    name = None
    period = None
    claim = None
    attorney = None

    def setup_profile(self, name, period):
        self.name = name
        self.period = period

    def claim(self, claim):
        claim = claim

    def attorney(self, name):
        attorney = name

    def print1(self):
        print(self.name, self.period)

    def print2(self):
        print(self.claim)

    def print3(self):
        print(self.period, self.attorney)
