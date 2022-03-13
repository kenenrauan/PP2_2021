h, a, b = input().split()
h = int(h)
a = int(a)
b = int(b)
ans = (h - a + (a - b) - 1) / (a - b) + 1
print(int(ans))
