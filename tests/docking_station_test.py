import pytest
from . import DockingStation
from . import Bike

dockingStation = DockingStation('Bank', 3)

class BikeTestDouble:
    def __init__(self, name):
        self.name = name
        self.broken = False

    def report_broken(self):
        self.broken = True
        return self.broken


bike = BikeTestDouble('bike1')
bike2 = BikeTestDouble('bike2')


def test_bike_can_be_added_to_docking_station():
    dockingStation.dock(bike, True)
    assert dockingStation.bikes == [bike]
    
def test_docking_station_does_not_release_bike_if_none_available():
    with pytest.raises(Exception):
       assert dockingStation.releaseBike()

def test_docking_station_doesnt_accept_more_bikes_than_their_capacity():
    for x in range(1,3):
        x = dockingStation.dock(bike)
    with pytest.raises(Exception):
       assert dockingStation.dock(bike)


def test_docking_station_wont_release_a_broken_bike():
    dockingStation.dock(bike, True)
    #dockingStation.releaseBike()
    with pytest.raises(Exception):
       assert dockingStation.releaseBike()