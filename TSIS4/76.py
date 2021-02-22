n = int(input())
a = input().split(maxsplit = n)
for i in range(0, len(a)):
	a[i] = int(a[i])
k = int(input())
if k < 0:
    k=abs(k)
    k = k % n
    print(*a[k:],end=" ")
    print(*a[0:k])
else:
    k=abs(k)
    k = k % n
    print(*a[-k:],end =" ")
    print(*a[0:-k])