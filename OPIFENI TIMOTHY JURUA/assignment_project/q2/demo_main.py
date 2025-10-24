from utils import math_utils, string_utils

def demo():
    print('Factorial 5 ->', math_utils.factorial(5))
    print('GCD 48,18 ->', math_utils.gcd(48, 18))
    print('Fibonacci(7) ->', math_utils.fibonacci(7))
    print('Vowels in "Hello World" ->', string_utils.count_vowels('Hello World'))
    print('Reverse "abcde" ->', string_utils.reverse_string('abcde'))

if __name__ == '__main__':
    demo()
