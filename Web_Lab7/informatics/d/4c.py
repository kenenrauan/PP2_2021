n = int(input())
a = input().split(maxsplit = n)
cnt = 0
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(0, len(a)):
	if a[i] > 0:
		cnt += 1
print(cnt)