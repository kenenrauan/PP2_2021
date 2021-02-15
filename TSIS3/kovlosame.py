a = input().split()
b = input().split()
cnt = 0
myset1 = set(())
myset2 = set(())
for i in a:
	myset1.add(i)
for i in b:
	myset2.add(i)
print(len(myset1.intersection(myset2)))