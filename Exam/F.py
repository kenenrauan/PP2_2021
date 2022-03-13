import math
a = input().split()
myset1 = set(())
myset2 = set(())
anslist = []
for i in range(0, len(a)):
	a[i] = int(a[i])
for i in a:
	myset1.add(i)
for i in range(0, len(a)):
	ans = int(math.log(a[i], 2) + 0.5)
	if 2 ** ans == a[i]: 
		myset2.add(a[i])

ansset = myset1.symmetric_difference(myset2)

for i in ansset:
	anslist.append(i)
anslist.sort(reverse=False)
for i in anslist:
	print(i, end=" ")
print()