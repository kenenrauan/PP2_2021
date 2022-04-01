n = int(input())
cnt = 0

from math import sqrt
for i in range(1, int(sqrt(n) + 1)):
    if n % i == 0:
        cnt += 1 + (n / i != i)

print(cnt)