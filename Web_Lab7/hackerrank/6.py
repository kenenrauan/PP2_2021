# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(y):
    leap = False
    
    leap = y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
    
    return leap

year = int(input())
print(is_leap(year))