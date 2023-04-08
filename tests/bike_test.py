import pytest
from . import Bike

bike = Bike()

def test_bike_isWorking():
    assert bike.isWorking() == True