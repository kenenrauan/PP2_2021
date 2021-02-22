n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
maxx = -1000000000000
for i in range(0, len(a)):
	if a[i] > maxx:
		maxx = a[i]
print(maxx)