from turtledemo.penrose import start

from src.toolkit.errors import CalculatorError
from src.toolkit.constans import OPERATORS, PRIORITY


def tokenizastion(expression: str) -> list[str]:
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == " ":
            i += 1
            continue
        if char in OPERATORS:
            i+=1
            tokens.append(char)
        elif char in "0123456789.":
            start = i
            while i < len(expression) and expression[i] in "0123456789.":
                i += 1
            tokens.append(expression[start:i])
            continue
        else:
            raise CalculatorError(message="Неккоректный символ",code_error="Invalid character in expression",)
    return tokens


def is_number(number:str) -> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False



def validate_tokenization(expression: str) -> None:
    expression = tokens = tokenizastion(expression)
    for i in range(len(tokens) - 1):
        if tokens[i].isdigit() and tokens[i+1].isdigit():
            raise CalculatorError(message="Нет оператора", code_error="no_operator")
        if tokens[i] in "*/" and tokens[i+1] in "*/":
            raise CalculatorError(message="Больше одного оператора", code_error=">1_operators")
    if not tokens:
        raise CalculatorError(message="Пустое выражение",code_error="empty_expression")
    if tokens[0] in"*/":
        raise CalculatorError(message="Первым идет число",code_error="number_is_fisrt")
    if tokens[-1] in "+-*/":
        raise CalculatorError(message="В конце идет число",code_error="number_in_the_end")




def _unar(tokens: list[str]) -> list[str]:
    i = 0
    while i < len(tokens):
        if tokens[i] in "+-":
            if (i == 0 or tokens[i-1] in "+-*/") and tokens[i+1].isdigit:
                tokens[i: i + 2] = [tokens[i] + tokens[i + 1]]
        i += 1
    return tokens



def to_rpn(tokens: list[str]) -> list[str]:
    stack = []
    result = []
    for token in tokens:
        if is_number(token):
            result.append(token)
            continue
        while stack and PRIORITY[stack[-1]] >= PRIORITY[token]:
            result.append(stack.pop())
        stack.append(token)
    while stack:
        result.append(stack.pop())
    return result


def solution(tokens: list[str]) -> float:
    result: list[float] = []
    for token in tokens:
        if is_number(token):
            result.append(float(token))
        else:
            if len(result) < 2:
                raise RuntimeError("Не хватает операндов")

            first = result.pop()
            second = result.pop()
            result.append(apply_operations(first, second, token))

    if len(result) != 1:
        raise RuntimeError("Должно остаться только одно значение")
    return float(result[0])


def apply_operations(a: float, b:float, operator: str) -> float:
    # Преобразуем строки в числа
    if  operator == '+':
        return a + b
    elif operator == '-':
        return b - a
    elif operator == '*':
        return a * b
    elif operator == '/':
        if a == 0:
            raise CalculatorError(message="Деление на ноль запрещено",code_error="devide_by_zero")
        else:
            return b/a
    else:
        raise CalculatorError(message="Неподдерживаемый оператор",code_error="invalid_operation")

def evaluate(expression: str) -> float:
    tokens = validate_tokenization(expression)
    tokens = _unar(tokenizastion(expression))
    rpn_tokens = to_rpn(tokens)
    return solution(rpn_tokens)


