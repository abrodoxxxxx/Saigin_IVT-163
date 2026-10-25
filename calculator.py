def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

if __name__ == "__main__":
    print(f"Сумма 5 и 3 = {add(5, 3)}")
    print(f"Разность 5 и 3 = {subtract(5, 3)}")
    print(f"Произведение 5 и 3 = {multiply(5, 3)}")