
def my_rest(sequence):
    """Возвращает последовательность без первого элемента или None, если последовательность пуста."""
    if not sequence:
        return None
    return sequence[1:]


print(my_rest([1, 2, 3, 4]))  
print(my_rest([]))             

def gcd(a, b):
    """Вычисляет наибольший общий делитель (НОД) двух чисел с использованием сопоставления с образцом."""
    match (a, b):
        case (0, _):
            return b
        case (_, 0):
            return a
        case _:
            return gcd(b, a % b)


print(gcd(48, 18))  
print(gcd(17, 5))   
print(gcd(60, 48))  