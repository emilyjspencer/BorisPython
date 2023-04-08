#from . import Bike

class DockingStation:


    def __init__(self, location):
        self.location = location
        self.bikes = []

    def releaseBike(self):
        if len(self.bikes) <= 0:
           raise Exception("Unable to release bike. None available")
        else:
            return self.bikes.pop()

    def dock(self, bike):
        self.bikes.append(bike)
        return self.bikes

   