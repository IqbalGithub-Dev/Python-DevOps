import pytest
from vault import Security_System

@pytest.fixture
def vault():
    return Security_System()

def test_happy_Path(vault):
    vault.enter_Code("iqbal786")
    assert vault.failed_attempt == 0
    assert not vault.is_Lock
def test_wrong_Password_Entered(vault):
    for i in range(3):
        with pytest.raises(ValueError):
            vault.enter_Code("BADPASSWORD123")
    assert vault.failed_attempt == 3
    assert vault.is_Lock == True
    
def test_Lock_The_Vault(vault):
    for i in range(3):
        with pytest.raises(ValueError):
            vault.enter_Code("BADPASSWORD123")
    with pytest.raises(PermissionError):
        vault.enter_Code("iqbal786")
