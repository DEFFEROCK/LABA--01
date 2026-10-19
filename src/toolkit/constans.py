from src.toolkit.errors import ConverterError

#операторы
OPERATORS: tuple[str, ...] = ("+", "-", "*", "/")

#приоритеты
PRIORITY: dict[str, int] = {
    "+": 0 ,
    "-": 0 ,
    "*": 1 ,
    "/": 1 ,
}

#величины длины
LENTH_PART: dict[str, float] = {
    "mm" : 0.001 ,
    "cm" : 0.01,
    "m": 1.0 ,
    "km": 1000.0,
}



#величины массы
WIDTH_PART: dict[str, float] = {
    "g" : 0.001 ,
    "kg" : 1.0 ,
}


#величины температуры
TEMPERATURE_PART: dict[str, str] = {
    "c": "Цельсия",
    "f": "Фаренгейт",
    "k": "Кельвин",
}

#все части единиц измерения
PARTS: list[dict] = [LENTH_PART, WIDTH_PART, TEMPERATURE_PART]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    '''
    Функция convert_temperature() преобразует температуру между градусами Цельсия, Фаренгейта и Кельвина. 
    Она приводит обозначения единиц измерения к нижнему регистру, выполняет соответствующие вычисления и возвращает результат типа float. 
    Если исходная и целевая единицы совпадают, значение не изменяется.
    '''

    #Единицы измерения одинаковые (C->C, F->F, K->K)
    if from_unit == to_unit:
        result = value
    #Из других единиц измерения в цельсии (F->C, K->C)
    elif from_unit == "f" and to_unit == "c":
        result = (value - 32) * 5/9
    elif from_unit == "k" and to_unit == "c":
        result = value - 273.15
    #Из цельсий в другие едницы измерения (C->F, C->K)
    elif from_unit == "c" and to_unit == "f":
        result  = value * 9 / 5 + 32
    elif from_unit == "c" and to_unit == "k":
        result = value + 273.15
    #Перевод между фаренгейтами и кельвинами (F->K, K->F)
    elif from_unit == "f" and to_unit == "k":
        result = (value -32)*5/9 +273.15
    else:
        result = (value -273.15)*9/5 + 32
    return float(result)

