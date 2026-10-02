import sys
import time
sys.set_int_max_str_digits(9000)
 
a = int('7' * 4301)
b = int('9' * 4300)

def gsd(a: int, b: int) -> list[int]:
    counter = 0
    while b != 0:
        a, b = b, a % b
        counter += 1
    print(f"count: {counter}")
    return abs(a)

result = gsd(a,b)
end_time = time.perf_counter()    

print(f"gsd(a,b)= {result}, end time: {end_time}")
