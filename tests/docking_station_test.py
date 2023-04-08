import pytest
from . import DockingStation
from . import Bike

dockingStation = DockingStation('Bank', 3)
bike = Bike()


def test_bike_can_be_added_to_docking_station():
     
    dockingStation.dock(bike)
    assert dockingStation.bikes == [bike]
    
def test_docking_station_does_not_release_bike_if_none_available():
    dockingStation.releaseBike()
    with pytest.raises(Exception):
       assert dockingStation.releaseBike()

def test_docking_station_doesnt_accept_more_bikes_than_their_capacity():
    dockingStation.dock(bike)
    dockingStation.dock(bike)
    dockingStation.dock(bike)
    dockingStation.dock(bike)
    with pytest.raises(Exception):
       assert dockingStation.dock(bike)

    