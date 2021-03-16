f = open('test.txt', 'a')
f.write("Today is Thursday")
f.close()

f = open('test.txt', 'r')
print(f.read())