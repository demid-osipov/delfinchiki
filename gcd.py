"""какой-то сложный древнегреческий алгоритм"""

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return gcd(y, x%y)

print(gcd(int(input()),int(input())))
