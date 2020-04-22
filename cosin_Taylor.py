import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

iterations = 20

def my_cos(x):
    """Вычисление косинуса с помощью ряда Маклорена"""
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range (1, iterations):
        x_pow *= x**2
        multiplier *= -1/(2*n-1)/(2*n)
        partial_sum += x_pow * multiplier

    return partial_sum

complex_angle = cmath.acos(10)

print (help(math.cos), math.cos(0.4))
print (help(my_cos), my_cos(0.4))

print ('"Угол", на котором косинус достигает 10:', complex_angle)
print ("Достигает ли 10 наш косинус?", my_cos(complex_angle))
print ("А библиотечный?", cmath.cos(complex_angle))

## %matplotlib inline

angles = np.r_[-16.00:16.00:0.01]
plt.plot(angles, np.cos(angles))
plt.plot(angles, np.vectorize(my_cos)(angles))
plt.show()
