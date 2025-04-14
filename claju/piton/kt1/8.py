def guess_number():
    print("Загадайте число, а я попробую его угадать!")
    n = int(input("Введите начало диапазона (n): "))
    m = int(input("Введите конец диапазона (m): "))
    
    attempts = 0
    while n <= m:
        attempts += 1
        guess = (n + m) // 2
        response = input(f"Ваше число {guess}? (больше/меньше/угадал): ").lower()
        
        if response == "угадал":
            print(f"Я угадал ваше число {guess} за {attempts} попыток!")
            return
        elif response == "больше":
            n = guess + 1
        elif response == "меньше":
            m = guess - 1
        else:
            print("Пожалуйста, введите 'больше', 'меньше' или 'угадал'.")
    
    print("Кажется, вы где-то ошиблись, я не смог угадать число.")

# Запуск игры
if __name__ == "__main__":
    guess_number()