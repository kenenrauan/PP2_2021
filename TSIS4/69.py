n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
a.reverse()
for i in range(0, len(a)):
	print(a[i], end = ' ')