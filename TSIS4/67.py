n = int(input())
a = input().split(maxsplit = n)
cnt = 0
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(0, len(a) - 1):
	if a[i] > 0:
		if a[i + 1] > 0:
			cnt = 1
	elif a[i] < 0:
		if a[i + 1] < 0:
			cnt = 1
if cnt == 1:
	print("YES")
else :
	print("NO")
