a = input().split()
b = input().split()
k = int(input())
ans = 0
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in range(0, len(b)):
	b[i] = int(b[i])
for i, j in zip(a, b):
	if k >= i and k <= j:
		ans += 1
print(ans)
