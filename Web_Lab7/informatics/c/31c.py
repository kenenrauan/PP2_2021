from math import sqrt
print(*(lambda a, b: filter(lambda x: int(sqrt(x)) * int(sqrt(x)) == x, range(a, b + 1)))( int(input()), int(input()) ))