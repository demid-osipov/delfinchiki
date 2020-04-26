import timeit
import_module = "import functools"

testcode = '''
@functools.lru_cache()
def fib_fast(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_fast(n-1) + fib_fast(n-2)

for n in range(1, 16):
    fib_fast(n)
'''

print(timeit.timeit(stmt = testcode, setup = import_module, number = 1000))
