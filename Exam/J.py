a,b = input().split()
a = int(a)
b = int(b)
anslist = []
for i in range(a, b + 1):
	check = False
	if i != 1:
		for j in range(2, i):
			if i % j == 0:
				check = True
				break
		if not check:
			anslist.append(i)

anslist.sort(reverse=True)
for i in anslist:
	print(i, end=' ')

print()