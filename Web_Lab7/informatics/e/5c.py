def xor(x: bool, y: bool) -> bool:
    return x != y

print(int(xor(*map(int, input().split()))))