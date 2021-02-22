def reverse(arr, l, r):
	while l < r:
		arr[l], arr[r] = arr[r], arr[l]
		l += 1
		r -= 1
	return arr
n, a, b, c, d = [int(i) for i in input().split()]
arr = [i for i in range(1, n + 1)]
reverse(arr, a - 1, b - 1)
reverse(arr, c - 1, d - 1)

for i in arr:
	print(i, end = " ")
