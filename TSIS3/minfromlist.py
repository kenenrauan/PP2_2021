a = list(map(int, input().split()))
mini = 9999
for i in range(0, len(a)):
	if a[i] > 0:
		if a[i] < mini:
			mini = a[i]
print(mini)
