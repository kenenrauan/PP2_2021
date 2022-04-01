def min_4_int(a: int, b: int, c: int, d: int) -> int:
    return min(a, b, c, d)

print(min_4_int(*map(int, input().split())))