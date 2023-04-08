class Bike:

    def __init__(self, name):
        self.broken = False
        self.name = name

    def isWorking(self):
       self.broken = False
       return self.broken