
n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(0, len(a)):
	if a[i] % 2 == 0:
		print(a[i], end = ' ')