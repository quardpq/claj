from functools import partial, reduce


words = partial(str.split, sep=" ")


filter_qs = partial(filter, lambda x: 'q' in x)


def keep_highest(x, y):
    return x if x >= y else y

maximum = partial(reduce, keep_highest)


print(words("hello world"))  
print(list(filter_qs(["quick", "brown", "fox", "queue"])))  
print(maximum([3, 1, 4, 1, 5, 9])) 