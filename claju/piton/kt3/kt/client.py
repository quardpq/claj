import requests
import sys

BASE_URL = 'http://localhost:5000'

def print_menu():
    print("\nURL Shortener Menu:")
    print("1. Создать короткий URL")
    print("2. Показать оригинальный URL")
    print("3. Изменить оригинальный URL")
    print("4. Удалить URL")
    print("5. Выйти")

def create_short_url():
    normal_url = input("Введите оригинальный URL: ")
    response = requests.post(f"{BASE_URL}/normal-url", json={'normal_url': normal_url})
    
    if response.status_code in (200, 201):
        data = response.json()
        print(f"Короткий URL: {data['short_url']}")
    else:
        print("Ошибка:", response.json().get('error', 'Unknown error'))

def get_normal_url():
    short_url = input("Введите короткий URL: ")
    response = requests.get(f"{BASE_URL}/short-url/{short_url}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Оригинальный URL: {data['normal_url']}")
    else:
        print("Ошибка:", response.json().get('error', 'Not found'))

def update_url():
    short_url = input("Введите короткий URL для изменения: ")
    new_normal_url = input("Введите новый оригинальный URL: ")
    
    response = requests.put(
        f"{BASE_URL}/short-url/{short_url}",
        json={'normal_url': new_normal_url}
    )
    
    if response.status_code == 200:
        print("URL успешно обновлен")
    else:
        print("Ошибка:", response.json().get('error', 'Unknown error'))

def delete_url():
    short_url = input("Введите короткий URL для удаления: ")
    response = requests.delete(f"{BASE_URL}/short-url/{short_url}")
    
    if response.status_code == 200:
        print("URL успешно удален")
    else:
        print("Ошибка:", response.json().get('error', 'Unknown error'))

def main():
    while True:
        print_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            create_short_url()
        elif choice == '2':
            get_normal_url()
        elif choice == '3':
            update_url()
        elif choice == '4':
            delete_url()
        elif choice == '5':
            print("Выход из программы")
            sys.exit(0)
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()