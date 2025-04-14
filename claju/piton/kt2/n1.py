
def squares():
    n = 0
    while True:
        yield n * n
        n += 1


def factorial_seq():
    n = 1
    acc = 1
    while True:
        yield acc
        n += 1
        acc *= n


def triangular_numbers():
    n = 1
    acc = 1
    while True:
        yield acc
        n += 1
        acc += n


if __name__ == "__main__":
    # Задание 1
    sq_gen = squares()
    print("Квадраты чисел:", [next(sq_gen) for _ in range(5)])  

    # Задание 2
    fact_gen = factorial_seq()
    print("Факториалы:", [next(fact_gen) for _ in range(5)])  

    # Задание 3
    tri_gen = triangular_numbers()
    print("Треугольные числа:", [next(tri_gen) for _ in range(5)]) 