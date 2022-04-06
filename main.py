file1 = open('test.txt', 'r')
print(file1.read())
file1.close()

file1 =  open('test.txt', 'a')
file1.write("\n Tomorrow")
file1.close()

file1 = open('test.txt', 'r')
print(file1.read())
file1.close()
