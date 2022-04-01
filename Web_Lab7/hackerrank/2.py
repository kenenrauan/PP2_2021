# https://www.hackerrank.com/challenges/py-if-else/problem
s = ''

n = int(input())

if n % 2 == 1:
    s = 'Weird'
elif n <= 4 or n > 20:
    s = 'Not Weird'
else:
    s = 'Weird'

print(s)
