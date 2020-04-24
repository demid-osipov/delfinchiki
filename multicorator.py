def repeat(n):
    def first_step(initialFunc):
        def second_step(result):
            for i in range(n):
                result = initialFunc(result)
            return result
        return second_step
    return first_step

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mult_2(x):
    return x * 2


print(plus_1(3))  # должно выдать 5
print(mult_2(4))  # должно выдать 4
