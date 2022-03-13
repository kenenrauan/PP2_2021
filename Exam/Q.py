n, m = input().split()
n = int(n)
m = int(m)
arr = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
	for j in range(m):
		if (i < n // 2 and j < m // 2):
			arr[i][j] = 1
		elif (i < n // 2 and j > ((m // 2) - 1)):
			arr[i][j] = 0
		elif (i >= (n // 2) and j < m // 2):
			arr[i][j] = 2
		elif (i >= (n // 2) and j > ((m // 2) - 1)):
			arr[i][j] = 3

for i in range(n):
	for j in range(m):
		print(arr[i][j], end = ' ')
	print()
