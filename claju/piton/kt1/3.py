def create_greeting(name):
    """Добавляет префикс 'Многоуважаемый(ая)' перед именем"""
    return f"Многоуважаемый(ая) {name}"


def create_vladivostok_address(name, street, house_number, apartment_number):
    """
    Создает полный почтовый адрес для Владивостока.
    Включает приветствие, город, улицу, номер дома и квартиры.
    """
    greeting = create_greeting(name)
    city = "г. Владивосток"
    address = f"{street}, д. {house_number}, кв. {apartment_number}"
    full_address = f"{greeting},\n{city}, {address}"
    return full_address


def get_location(name, street, house_number, apartment_number, city="Владивосток"):
    """
    Определяет местоположение и формирует полный почтовый адрес.
    По умолчанию используется Владивосток.
    """
    if city == "Владивосток":
        return create_vladivostok_address(name, street, house_number, apartment_number)
    else:
        return f"Адрес не поддерживается для города {city}"


if __name__ == "__main__":

    name = "Иванова Мария Сергеевна"
    street = "ул. Светланская"
    house_number = 12
    apartment_number = 45


    address = get_location(name, street, house_number, apartment_number)
    print(address)

  
    other_city_address = get_location(name, street, house_number, apartment_number, city="Москва")
    print(other_city_address)