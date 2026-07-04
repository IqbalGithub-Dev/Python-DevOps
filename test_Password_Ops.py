import pytest
from password_Ops import is_Strong_Password

def test_Short_Password():
    assert not is_Strong_Password("iqbal")
def test_Nospecial_Char():
    assert not is_Strong_Password("iqbalsazid")
def test_perfect_Password():
    assert is_Strong_Password("Iqbal@1998!")