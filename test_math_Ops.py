from math_Ops import add_number, sub_number

def test_addition():
    assert add_number(10, 5) == 15

# The new test that forces Line 4 to execute
def test_subtraction():
    assert sub_number(10, 5) == 5