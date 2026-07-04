import pytest
from smart_Home import smartBulb


@pytest.fixture
def living_Room_Bulb():
    return smartBulb()

def test_bulb_Turns_On(living_Room_Bulb):
    living_Room_Bulb.turn_On()
    assert living_Room_Bulb.is_On == True
    assert living_Room_Bulb.Brightness == 100
    
def test_bulb_Turns_off(living_Room_Bulb):
    living_Room_Bulb.trun_Off()
    assert living_Room_Bulb.is_On == False
    assert living_Room_Bulb.Brightness == 0