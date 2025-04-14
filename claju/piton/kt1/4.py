from functools import partial


def if_even(func, n):
    if n % 2 == 0:
        return func(n)
    else:
        return n


if_even_inc = partial(if_even, lambda x: x + 1)
if_even_double = partial(if_even, lambda x: x * 2)
if_even_square = partial(if_even, lambda x: x ** 2)


print(if_even_inc(4))  
print(if_even_double(4))  
print(if_even_square(4))  
print(if_even_inc(3)) 


def binary_partial(func, arg1):
    return lambda arg2: func(arg1, arg2)


add = lambda x, y: x + y
add_five = binary_partial(add, 5)
print(add_five(10))  

multiply = lambda x, y: x * y
multiply_by_three = binary_partial(multiply, 3)
print(multiply_by_three(7))  