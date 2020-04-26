import timeit

testcode = '''
def fib(n):
        if n == 1:
                return 1
        elif n == 2:
                return 1
        else:
                return fib(n-1) + fib(n-2)

for n in range(1, 16):
    fib(n)
'''
     
print(timeit.timeit(stmt = testcode, number = 1000))
