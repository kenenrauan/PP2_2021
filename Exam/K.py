import math
a = input().split()
myset = set(())
anslist = []
for i in range(0, len(a)):
	a[i] = int(a[i])
a.sort(reverse=False)
for i in range(0, len(a)):
	ans = int(math.log(a[i], 2) + 0.5)
	if 2 ** ans == a[i]:
		myset.add(a[i])

for i in myset:
	anslist.append(i)
anslist.sort(reverse=False)
for i in anslist:
	print(i, end = ' ')
print()