#from . import Bike

class DockingStation:


    def __init__(self, location):
        self.location = location
        self.bikes = []

    def releaseBike(self):
        return "Bike"

    def dock(self, bike):
        self.bikes.append(bike)
        return self.bikes