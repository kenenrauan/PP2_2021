mylist = []
a, b, k = input().split()
a = int(a)
b = int(b)
k = int(k)
for i in range(1, min(a, b) + 1):
	if a % i == 0 and b % i == 0:
		mylist.append(i)
print(mylist[len(mylist) - k])