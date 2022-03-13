myset = set(())
n = input().split()
ansset = set(())
ans = []
for i in range(0, len(n)):
	n[i] = int(n[i])

check = False

for i in n:
	if i in myset:
		if i not in ansset:	
			if i > 1:
				for y in range(2, i):
					if i % y == 0:
						check = True
						break
			if check:
				ansset.add(i)
			check = False
	myset.add(i)
for i in ansset:
	ans.append(i)
for i in ans:
	print(i, end=' ')
print()