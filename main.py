import random
import math

total = 0
inside = 0

for x in range(1_000_000_000):
     x = random.random()
     y = random.random()
     total += 1

     if math.dist([x, y], [0, 0]) <= 1:
             inside += 1

pi_value = (inside / total) * 4

print(pi_value)