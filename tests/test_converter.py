import pytest
from src.toolkit.converter import _converter
from src.toolkit.errors import ConverterError

@pytest.mark.parametrize(
    ("value", "from_unit", "to_unit", "final_result"),
    [
        (5.0, "kg", "g", 5000.0),
        (0.0, "c", "k", 273.15),
        (6000.0, "mm", "m", 6.0),
        (800.0, "G", "Kg", 0.8),
        (0.0, "K  ", "     C ", -273.15),
        (9.7, "  KM", "m ", 9700.0),
        (17.0, "cm", "mM", 170.0),
        (155.0, "c", "f", 311),
        (113, "F","K  ",318.15),
        (13.6, "kg","kG ",13.6),
        (280, "k","K   ",280)
    ],
)
def test_converter_positive(value: float, from_unit: str, to_unit: str, final_result: float) -> None:
    assert _converter(value, from_unit, to_unit) == pytest.approx(final_result)

@pytest.mark.parametrize(
    ("value", "from_unit", "to_unit", "code_error"),
    [
        (-6, "kg", "g", "negative_value"),
        (0.0, "celcius", "k", "incorrect_unit"),
        (145, "mm", "kg", "different_parts"),
        (800.0, " ", "Kg", "incorrect_unit"),
        (-1.0, "K  ", "  C ", "temp_below_zero"),
        (-274, "C  ", "     K ", "temp_below_zero")
    ],
)
def test_converter_negative(value: float, from_unit: str, to_unit: str, code_error: str) -> None:
    with pytest.raises(ConverterError) as warn:
        _converter(value, from_unit, to_unit)
    assert warn.value.code_error == code_error





