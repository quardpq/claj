import sys

def sum_numbers():
    if len(sys.argv) < 2:
        print("Ошибка: не переданы числа для суммирования")
        print("Использование: python sum.py <число1> <число2> ...")
        return
    
    total = 0
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            total += num
        except ValueError:
            print(f"Ошибка: аргумент '{arg}' не является целым числом")
            return
    
    print(f"Сумма чисел: {total}")

if __name__ == "__main__":
    sum_numbers()