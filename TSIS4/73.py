n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
thisset = set(())
for i in a:
	thisset.add(i)
print(len(thisset))

