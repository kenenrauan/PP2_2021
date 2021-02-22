n = int(input())
a = input().split(maxsplit = n)
cnt = 0
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(1, len(a) - 1):
	if a[i] > a[i - 1]:
		if a[i] > a[i + 1]:
			cnt += 1
print(cnt)
