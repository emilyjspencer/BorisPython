import pytest
from . import Bike

bike = Bike('bike1')

def test_bike_reportAsBroken():
    assert bike.reportAsBroken() == True