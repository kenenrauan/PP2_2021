import math
a, b = input().split()
a = int(a)
b = int(b)
anslist = []
for i in range(a, b):
	i = str(i)
	if len(i) == 4:
		i = int(i)
		ans = int(math.log(i, 3) + 0.5)
		if 3 ** ans == i:
			anslist.append(i)
anslist.reverse()
for i in anslist:
	print(i, end=' ')
print()