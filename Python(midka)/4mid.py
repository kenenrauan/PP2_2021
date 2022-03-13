a = input().split()
ans = 0
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(0, len(a) - 1):
	for j in range(i + 1, len(a)):
		if a[i] == a[j]:
			ans += 1
print(ans)