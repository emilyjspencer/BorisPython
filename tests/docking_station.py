
class DockingStation:


    def __init__(self, location, maxCapacity):
        self.location = location
        self.bikes = []
        self.maxCapacity = 3

    def releaseBike(self):
        if len(self.bikes) <= 0:
           raise Exception("Unable to release bike. None available")
        else:
            return self.bikes.pop()

    def dock(self, bike):
        if len(self.bikes) > 3:
            raise Exception("Unable to dock bike. At maximum capacity")
        else: 
            self.bikes.append(bike)
            return self.bikes

   