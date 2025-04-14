
def repeat(value):
    """Бесконечно повторяет переданное значение."""
    while True:
        yield value


repeater = repeat(5)
for _ in range(10):
    print(next(repeater)) 


def subseq(start, end, sequence):
    """Возвращает подпоследовательность от start до end."""
    return sequence[start:end]


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(subseq(2, 6, sequence))  

string = "Hello, World!"
print(subseq(7, 12, string))  