
class DockingStation:


    def __init__(self, location, maxCapacity = 3):
        self.location = location
        self.bikes = []
        self.maxCapacity = maxCapacity

    def setMaxCapacity(self, value):
        self._maxCapacity = value

    def releaseBike(self):
        if not self.empty():
            if len(self.bikes)== 0:
                return bikes.pop()
            else:
                raise Exception("Unable to release a broken bike")
        else: raise Exception("Unable to release bike. None available")
            

    def dock(self, bike, broken = False):
        if self.full():
            raise Exception("Unable to dock bike. At maximum capacity")
        elif broken == True: 
            self.bikes.append(bike)
            return self.bikes

    def full(self):
        if len(self.bikes) >= 3:
            return True
        else:
            return False

    def empty(self):
        if len(self.bikes) == 0:
            return True
        else:
            return False
