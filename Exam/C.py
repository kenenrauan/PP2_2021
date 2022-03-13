a = input().split()
cnt = 0
for i in a:
	if i == '0':
		cnt += 1
	else:
		print(i, end = ' ')
print('0 ' * cnt)