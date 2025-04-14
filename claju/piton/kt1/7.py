
def reverse(sequence):
    """Возвращает список в обратном порядке."""
    reversed_sequence = []
    for item in sequence:
        reversed_sequence.insert(0, item)
    return reversed_sequence

print(reverse([1, 2, 3, 4]))  
print(reverse(["a", "b", "c"])) 


def reverse_slice(sequence):
    """Возвращает список в обратном порядке."""
    return sequence[::-1]


print(reverse_slice([1, 2, 3, 4]))  
print(reverse_slice(["a", "b", "c"]))  


def fibonacci(n):
    """Возвращает список из первых n чисел Фибоначчи."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


print(fibonacci(10))


def fibonacci_recursive(n):
    """Возвращает n-е число Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(10))  