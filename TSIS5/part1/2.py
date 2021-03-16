def file_read(fname):
   txt = open(fname)
   print(txt.readline())
   
file_read('test.txt')