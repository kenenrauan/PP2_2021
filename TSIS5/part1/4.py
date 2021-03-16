n = int(input())
k = 0
f = open("test.txt", "r")
for x in f:
  k += 1
  if k >= n:
  	print(x)

