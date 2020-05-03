import taylor
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

iterations = 20

complex_angle = cmath.acos(10)

print (help(math.cos), math.cos(0.4))
print (help(taylor.tcos), taylor.tcos(0.4, iterations))

print ('"Угол", на котором косинус достигает 10:', complex_angle)
print ("Достигает ли 10 наш косинус?", taylor.tcos(complex_angle, iterations))
print ("А библиотечный?", cmath.cos(complex_angle))

## %matplotlib inline

angles = np.r_[-16.00:16.00:0.01]
plt.plot(angles, np.cos(angles))
plt.plot(angles, np.vectorize(taylor.tcos)(angles, iterations))
plt.show()
