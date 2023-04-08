import pytest
from . import DockingStation
from . import Bike

dockingStation = DockingStation('Bank')
bike = Bike()

def test_docking_station_releaseBike():
    assert dockingStation.releaseBike() == "Bike"

def test_bike_can_be_added_to_docking_station():
     
    dockingStation.dock(bike)
    assert dockingStation.bikes == [bike]
    

