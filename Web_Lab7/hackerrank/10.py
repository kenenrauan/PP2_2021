# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(input().split())
x = (set(input().split()) for _ in range(int(input())))

print(all(map(lambda s: len(a.difference(s)) != 0 and len(s.difference(a)) == 0, x)))    