class Bike:

    def __init__(self, name):
        self.broken = False
        self.name = name

    def reportAsBroken(self):
       self.broken = True
       return self.broken