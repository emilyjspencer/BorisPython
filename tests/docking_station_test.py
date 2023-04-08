import pytest
from . import DockingStation
from . import Bike

dockingStation = DockingStation('Bank', 3)
bike = Bike('bike1')


def test_bike_can_be_added_to_docking_station():
     
    dockingStation.dock(bike)
    assert dockingStation.bikes == [bike]
    
def test_docking_station_does_not_release_bike_if_none_available():
    dockingStation.releaseBike()
    with pytest.raises(Exception):
       assert dockingStation.releaseBike()

def test_docking_station_doesnt_accept_more_bikes_than_their_capacity():
    for x in range(1,4):
        x = dockingStation.dock(Bike('1'))
        bike4 = Bike('bike4')
    with pytest.raises(Exception):
       assert dockingStation.dock(bike3)

#def test_docking_station_can_set_maximum_capacity():


#def test_docking_station_wont_release_a_broken_bike():
    