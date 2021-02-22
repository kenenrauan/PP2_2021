n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
print(a[len(a) - 1], end = ' ')
for i in range(0, len(a) - 1):
	print(a[i], end = ' ')

