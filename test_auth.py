import pytest
from auth import is_Valid_Password

@pytest.mark.parametrize("bad_password", [
    "short","123450","onlyletters",""
])

def test_bad_password_test(bad_password):
    result =  is_Valid_Password(bad_password)
    assert result == False