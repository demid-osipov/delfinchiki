import numpy as np

def gauss(a, b):
    rowq = len(a)

    def forward():        
        for i in range(rowq):
            b[i] = b[i] / a[i][i]
            a[i] = a[i] / a[i][i]
            for j in range(i+1, rowq):
                b[j] -= b[i] * a[j][i]
                a[j] -= a[i] * a[j][i]
        pass

    def backward():
        x = np.zeros(len(b))
        for i in range(rowq-1, -1, -1):
            x[i] = b[i] - sum([a[i][j] * x[j] for j in range(i + 1, rowq)])
        return x

    forward()
    return backward()



a = np.array([
    [1,2,1],
    [3,2,0],
    [1,0,0]
], dtype=np.float)

b = np.array([5,6,7], dtype=np.float)

print(gauss(a, b))
