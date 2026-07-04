import pytest
from add import calculator


@pytest.fixture
def setup_calculator():
    calc = calculator()
    yield calc

@pytest.mark.smoke
@pytest.mark.parametrize(
    "num1,num2,expected_result",
    [(5, 4, 9), (2, -1, 1), (-5, -1, -6), (4, -6, -2), (5, 0, 5)],
)
def test_add_sum(setup_calculator, num1, num2, expected_result):
    calc = setup_calculator
    result = calc.sum(num1, num2)
    assert result == expected_result

@pytest.mark.regression
@pytest.mark.parametrize(
    "num1,num2,Expected_result",
    [(-4, 2, -2), (-8, -2, 4), (50, 10, 5), (5, 2, 2.5),(0,2000,0)],
)
def test_div_test(setup_calculator, num1, num2, Expected_result):
    calc = setup_calculator
    assert calc.div(num1, num2) == Expected_result

def test_negative_test(setup_calculator):
    calc = setup_calculator
    with pytest.raises(ZeroDivisionError):
        calc.div(5/0)
        

