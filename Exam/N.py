s = input()
s2 = input()
ans1 = ''.join(sorted(s))
ans2 = ''.join(sorted(s2))
if ans1 == ans2:
	print("YES")
else:
	print("NO")