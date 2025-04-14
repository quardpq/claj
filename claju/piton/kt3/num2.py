import json
import os

books_by_year = {
    2021: {
        "Программирование на Clojure": {"цена": 100, "количество": 10},
        "Backend в IThub": {"цена": 400, "количество": 5}
    },
    2022: {
        "JavaScript для начинающих": {"цена": 150, "количество": 8},
        "Python для анализа данных": {"цена": 300, "количество": 6}
    }
}

ORDERS_FILE = "orders.json"

def save_order(year, book_name, quantity, total_price):
    order = {
        "год": year,
        "название": book_name,
        "количество": quantity,
        "общая_цена": total_price
    }
    
    orders = load_orders()
    orders.append(order)
    
    with open(ORDERS_FILE, 'w') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    
    with open(ORDERS_FILE, 'r') as f:
        return json.load(f)

def calculate_price(book_name, year, quantity):
    return books_by_year[year][book_name]["цена"] * quantity

def show_confirmation(book_name, quantity, total_price):
    """Показывает подтверждение заказа"""
    print(f"\nПокупка {quantity} шт. {book_name} всего за: R{total_price:.1f}")

def show_orders():
    orders = load_orders()
    if not orders:
        print("\nНет сохраненных заказов")
        return
    
    print("\nСписок заказов:")
    for order in orders:
        print(f"Куплено {order['количество']} шт. {order['название']} за R{order['общая_цена']:.1f}")

def show_years_menu():
    print("\n| Доступные книги по годам |")
    years = list(books_by_year.keys())
    for i, year in enumerate(years, 1):
        print(f"{i}. {year}", end="  ")
    print()
    return years

def show_books_menu(year):
    print(f"\n| Книги за {year} |")
    books = list(books_by_year[year].keys())
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}", end="  ")
    print()
    return books

def order_book():
    years = show_years_menu()
    try:
        year_choice = int(input("Выберите год: ")) - 1
        if year_choice < 0 or year_choice >= len(years):
            raise ValueError
        year = years[year_choice]
    except (ValueError, IndexError):
        print("Неверный выбор года")
        return
    
    books = show_books_menu(year)
    try:
        book_choice = int(input("Выберите книгу: ")) - 1
        if book_choice < 0 or book_choice >= len(books):
            raise ValueError
        book_name = books[book_choice]
    except (ValueError, IndexError):
        print("Неверный выбор книги")
        return
    
    try:
        quantity = int(input("\nСколько экземпляров хотите приобрести?: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Неверное количество")
        return
    
    total_price = calculate_price(book_name, year, quantity)
    show_confirmation(book_name, quantity, total_price)
    save_order(year, book_name, quantity, total_price)

def main_menu():
    while True:
        print("\n|       Наши книги       |")
        print("| 1-Меню 2-Заказы 3-Выход|")
        
        try:
            choice = int(input("Выберите действие: "))
            if choice == 1:
                order_book()
            elif choice == 2:
                show_orders()
            elif choice == 3:
                print("Выход из программы")
                break
            else:
                print("Неверный выбор")
        except ValueError:
            print("Пожалуйста, введите число")

if __name__ == "__main__":
    main_menu()