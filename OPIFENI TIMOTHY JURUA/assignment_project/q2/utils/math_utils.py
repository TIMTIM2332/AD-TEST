def factorial(n):
    if n < 0:
        raise ValueError('n must be >= 0')
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def fibonacci(n):
    if n < 0:
        raise ValueError('n must be >= 0')
    seq = [0, 1]
    if n < 2:
        return seq[:n]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
