def pow(a: float, n: int) -> float:
    return a ** n

print(pow(*map(float, input().split())))