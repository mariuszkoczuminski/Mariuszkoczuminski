

import time

def suma(n):
    return sum(range(1, n+1))

start = time.time()
res = suma(10)
end = time.time()
print(res)
print(f"Czas wykonania: {end - start} sekund")

