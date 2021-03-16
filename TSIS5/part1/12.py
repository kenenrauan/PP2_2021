cars = ['Honda', 'Toyota']
f = open('test.txt', 'w')
for x in cars:
	 f.write(x)

f = open('test.txt', 'r')
print(f.read())