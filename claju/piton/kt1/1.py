def increment(n):
    """Увеличивает аргумент n на 1"""
    return n + 1

def double(n):
    """Удваивает значение аргумента n"""
    return n * 2

def square(n):
    """Возводит аргумент n в квадрат"""
    return n ** 2

def process_number(n):
    """
    Если n четное, возвращает n + 2;
    если нечетное, возвращает 3 * n - 1.
    """
    if n % 2 == 0:  
        return n + 2
    else:
        return 3 * n - 1
    

print(increment(5))       
print(double(4))          
print(square(3))          

print(process_number(4))  
print(process_number(5))  