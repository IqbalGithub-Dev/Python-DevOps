import pytest
from coffe import coffe_Machine

#Fixture setting
@pytest.fixture
def machine():
    return coffe_Machine()

# Test 1 - The Happy Path
def test_make_coffee_success(machine):
    machine.make_coffe()
    assert machine.water_Level == 80
    assert machine.bean_Level == 40

# Test 2 - The Empty Tank Alarm (Negative Testing)
def test_empty_tank_raises_error(machine):
    machine.water_Level = 0
    with pytest.raises(ValueError):
        machine.make_coffe(),"Water is GONE"