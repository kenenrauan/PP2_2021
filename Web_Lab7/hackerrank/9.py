# https://www.hackerrank.com/challenges/py-check-subset/problem

for t in range(int(input())):
    input()
    s1 = set(input().split())
    input()
    s2 = set(input().split())
    print(len(s1.difference(s2)) == 0)