n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
k = int(input())
for i in range(0, len(a)):
	if k > a[i]:
		print(i + 1)
		exit(0)
print(n + 1)

