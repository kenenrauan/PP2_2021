n = int(input())

arr = [[0] * n] * n
cnt = 0
for i in range(0, n):
	cnt = i
	for j in range(0, n, 1):
		arr[i][j] = cnt
		cnt += 1
for i in range(n):
	for j in range(n):
		print(arr[i][j], end= ' ')
	print()