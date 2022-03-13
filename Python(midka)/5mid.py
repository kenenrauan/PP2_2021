str = input()
c = input()
is_find_t = False
cur = 0
l = [0 for i in range(len(str))]
r = [0 for i in range(len(str))]
ans = []
sum = 0
for i in range(0, len(str)):
	if str[i] == c:
		is_find_t = 1
		cur = 0
	if is_find_t == 0:
		l[i] = 1e9
	else:
		l[i] = cur
		cur += 1

is_find_t = 0
cur = 0
for i in range(len(str) - 1, -1, -1):
	if str[i] == c:
		is_find_t = 1
		cur = 0
	if is_find_t == 0:
		r[i] = 1e9
	else:
		r[i] = cur 
		cur += 1
for i in l:
	print(i, end = ' ')
print()
for i in r:
	print(i, end = ' ')
print()
for i, j in zip(l, r):
	ans.append(min(i, j))

for i in ans:
	print(i, end=" ")
print()