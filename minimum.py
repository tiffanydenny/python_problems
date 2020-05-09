import random

minimum = [100]
for i in range(0, 9):
    number = random.randint(0, 100)
    if number < minimum:
        minimum = number


print(minimum)
