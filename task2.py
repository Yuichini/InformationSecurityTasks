import random 
import time

a = random.randint(0, 99877332288888)
b = random.randint(0, 779999880221)

def gsd(a: int, b: int) -> list[int]:
    counter = 0
    while b != 0:
        a, b = b, a % b
        counter += 1
    print(f"count: {counter}")
    return abs(a)

result = gsd(a,b)
end_time = time.perf_counter()    

print(f"gsd(a,b) = {result}, end time: {end_time}")
