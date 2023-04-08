import pytest
from . import DockingStation


dockingStation = DockingStation('Bank')

def test_docking_station_releaseBike():
    assert dockingStation.releaseBike() == "Bike"

