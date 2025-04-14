from functools import partial


is_last_in_stock = lambda cars: cars[-1].get("in_stock")


average = lambda xs: sum(xs) / len(xs)
average_dollar_value = lambda cars: average(map(lambda car: car.get("dollar_value"), cars))


fastest_car = lambda cars: sorted(cars, key=lambda car: car.get("speed"))[-1].get("name")


cars = [
    {"name": "Toyota", "in_stock": True, "dollar_value": 20000, "speed": 120},
    {"name": "Honda", "in_stock": False, "dollar_value": 30000, "speed": 150}
]

print(is_last_in_stock(cars))        
print(average_dollar_value(cars))     
print(fastest_car(cars))              