from functools import reduce

numbers = [2, 5, 8, 11, 14, 17, 20]

# 1. square each number using map
squares = list(map(lambda x: x*x, numbers))
print('Squares:', squares)

# 2. filter squares > 100
filtered = list(filter(lambda x: x > 100, squares))
print('Filtered (>100):', filtered)

# 3. reduce sum of remaining
total = reduce(lambda a,b: a+b, filtered, 0)
print('Sum of filtered squares:', total)
