from logging.config import valid_ident

from src.toolkit.errors import ConverterError
from src.toolkit.constans import PARTS, convert_temperature, TEMPERATURE_PART
from typing import Any


def check_part(unit: str) -> dict[str, Any]:
    parts = [part for part in PARTS if unit in part]
    if len(parts) > 1:
        raise RuntimeError("Неправильное исходное разбиение на части")
    if len(parts) == 0:
        raise ConverterError(message=f"некорректная единица измерения - '{unit}'", code_error = "incorrect_unit")
    return parts[0]

def validation(value: float,from_unit: str, to_unit: str) -> dict[str, float]:
    part_from = check_part(from_unit)
    part_to = check_part(to_unit)
    value = float(value)
    if part_from != part_to:
        raise ConverterError(message = "единицы измерения находятся в разных частях", code_error = "different_parts")
    if part_from !=  PARTS[2] and value < 0:
        raise ConverterError(message = "в этой части не может быть отрицальных чисел", code_error = "negative_value")
    if part_from == PARTS[2]:
        if (from_unit.lower().strip() == "c" and value < -273.15) or (from_unit.lower().strip()  == "k" and value < 0) or (from_unit.lower().strip()  == "f" and value < -459.67):
            if convert_temperature(value, from_unit, to_unit):
                raise ConverterError(message = "температура не можеть быть ниже абсолютного нуля", code_error = "temp_below_zero")
    return part_from

def _converter(value: float, from_unit: str, to_unit: str) -> float:
    from_unit, to_unit = from_unit.lower().strip(), to_unit.lower().strip()
    value = float(value)
    part = validation(value, from_unit, to_unit)
    if from_unit in TEMPERATURE_PART:
        new_temp = convert_temperature(value, from_unit, to_unit)
        return float(new_temp)
    return float(value*part[from_unit]/part[to_unit])





