class ToolkitError(Exception):
    """"Базовая ошибка Toolkit"""
    def __init__(self, message: str , code_error: str) -> None:
        super().__init__(message)
        self.code_error = code_error
class ConverterError(ToolkitError):
        """Ошибка конвертера"""
class CalculatorError(ToolkitError):
        """Ошибка калькулятора"""



