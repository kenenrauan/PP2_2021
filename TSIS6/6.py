def check_range(num, r1, r2):
    if num in range(r1, r2):
        print('Yes')
    else:
        print('No')

num, r1, r2 = [int(i) for i in input().split()]
check_range(num ,r1, r2)