import pytest
from src.toolkit.calculator import evaluate
from src.toolkit.errors import CalculatorError

@pytest.mark.parametrize(
    ("expression","result"),
    [
        ("1+-2",-1.0),
        ("5*6+-4",26.0),
        ("-7+-2",-9.0),
        ("2/4", 0.5),
        ("4.0+-7.0", -3.0),
        ("60/-15.0", -4.0),
        ("-86 + -100", -186.0),
        ("9 *- 5", -45.0),
        ("76.5/0.5", 153.0),
        ("2+-2*9/3+6", 2.0),
        ("121.0/11", 11.0),
        ("6- + 5", 1.0),
        ("1.5 - 9.7", -8.2)
    ],
)
def test_calculator_positive(expression: str, result: float) -> float:
    assert evaluate(expression) == pytest.approx(result)

@pytest.mark.parametrize(
    ("expression","code_error"),
    [
        ("1/0","devide_by_zero"),
        ("a + r723t0","Invalid character in expression"),
        ("15 43","no_operator"),
        ("49*/7",">1_operators"),
        ("*4","number_is_fisrt"),
        (" ","empty_expression"),
    ],
)
def test_calculator_negative(expression: str, code_error: str) -> None:
    with pytest.raises(CalculatorError) as warn:
        evaluate(expression)
    assert warn.value.code_error == code_error
