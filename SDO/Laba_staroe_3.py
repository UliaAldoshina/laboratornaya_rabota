import random

def generate_random_list(x, a, b):
    return [random.randint(a, b) for i in range(x)]

print(generate_random_list(5, 1, 10))
print(generate_random_list(3, 50, 100))
print(generate_random_list(7, -5, 5))