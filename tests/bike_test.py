import pytest
from . import Bike

bike = Bike('bike1')

def test_bike_isWorking():
    assert bike.isWorking() == False