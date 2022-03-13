my_list = []
def check(num):
	x = int(num)
	while x != 0:
		my_list.append(x%7)
		x = x//7
n = int(input())
if n == 0:
	print(0)
else:
	check(n)
	my_list.reverse()
	for i in range(0, len(my_list)):
		print(my_list[i], end='')
	print()