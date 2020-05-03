"""здесь всякие функции (пока только косинус) реализованы с помощью суммирования ряда Тейлора"""

def tcos(x, iterations):
    """Вычисление косинуса с помощью ряда Тейлора"""
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range (1, iterations):
        x_pow *= x**2
        multiplier *= -1/(2*n-1)/(2*n)
        partial_sum += x_pow * multiplier

    return partial_sum
