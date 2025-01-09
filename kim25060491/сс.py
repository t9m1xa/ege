def convert_number_system(number: int, base: int) -> str:
    """
    Конвертирует число из десятичной системы счисления в указанную систему счисления.

    :param number: Число в десятичной системе счисления.
    :param base: Целевая система счисления (от 2 до 36).
    :return: Строковое представление числа в целевой системе счисления.
    """
    # Символы для представления цифр и букв в разных системах счисления
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if not (2 <= base <= 36):
        raise ValueError("База системы счисления должна быть между 2 и 36.")
    
    converted = ""
    while number > 0:
        number, remainder = divmod(number, base)
        converted = digits[remainder] + converted
    return converted if converted else "0"

# Пример использования функции
print(convert_number_system(16, 2))   # Выводит: 10000
print(convert_number_system(16, 16))  # Выводит: 10
print(convert_number_system(255, 10))  # Выводит: 255
print(convert_number_system(255, 16)) # Выводит: FF