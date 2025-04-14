
increment = lambda n: n + 1

double = lambda n: n * 2

square = lambda n: n ** 2


process_number = lambda n: n + 2 if n % 2 == 0 else 3 * n - 1


print(increment(5))       
print(double(4))          
print(square(3))          
print(process_number(4))  
print(process_number(5))  


numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  