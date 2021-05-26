f = open('demoFile.txt', 'r')
print(f.read())
print('------------------------------------')
f1 = open('demoFile.txt')
line = f1.readline()
while line != "":
    print(line)
    line = f1.readline()
print('------------------------------------')
f2 = open('demoFile.txt')
for element in f2.readlines():
    print(element)
