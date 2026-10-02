import time 

def gsd(a: int, b: int) -> list[int]:
    counter = 0
    while b != 0:
        a, b = b, a % b
        counter += 1
    print(f"count: {counter}")
    return abs(a)

a, b = map(int, input("a, b: ").split())
result = gsd(a,b)

end_time = time.perf_counter()    

print(f"gsd(a,b) = {result}, end time: {end_time}")
