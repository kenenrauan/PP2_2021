import re
pattern = r'(1299|1[3-8]\d{2}|19([0-1]\d|2[0-2]))\s(0\d|1[0-2])\s([0-2]\d|3[0-1])'
txt = input()
x = re.search(pattern, txt)
if x:
    print('Yes')
else:
    print("No")
