
def conjoin(flock_a, flock_b):

    return flock_a + flock_b

def breed(flock_a, flock_b):

    return flock_a * flock_b


flock_a = 4
flock_b = 2
flock_c = 0


result = conjoin(
    conjoin(
        conjoin(flock_a, flock_c), 
        breed(flock_a, flock_b)    
    ),
    breed(conjoin(flock_a, flock_c), flock_b)  
)

print(result)  