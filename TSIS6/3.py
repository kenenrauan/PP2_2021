from math import prod
a = input().split()
for i in range(0, len(a)):
	a[i] = int(a[i])
print(prod(a))