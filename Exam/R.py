c = input()
s = input()
ans = str()
for i in range(0, len(s)):
	if s[i] != c:
		ans = ans + s[i]
print(ans)