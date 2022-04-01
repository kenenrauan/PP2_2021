n = int(input())
print('YES' if (n & (n - 1)) == 0 else 'NO')