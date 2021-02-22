n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(0, len(a) - 1):
	if i % 2 == 0:
		a[i], a[i + 1] = a[i + 1], a[i]
for i in range(0, len(a)):
	print(a[i], end = ' ')