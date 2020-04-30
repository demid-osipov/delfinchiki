"""сложный расширенный древнегреческий алгоритм"""

def egcd1(a, b):
    if b == 0:
        return (1, 0, a)
    y, x, gcd = egcd1(b, a%b)
    return (x, y - (a//b)*x, gcd)

print(egcd1(int(input()), int(input())))
