# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

n, m = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.max(numpy.min(a, axis = 1)))