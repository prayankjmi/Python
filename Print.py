import sys

file = open (r'E:\Python\Code\Data\Data.txt', 'r')
#print (file.read())

#print (file.readline())

D={}

for line in open (r'E:\Python\Code\Data\Data.txt', 'r'):
    data = line.rstrip().split(',')
    if not data[2].isdigit():
        pass
    elif data[3] in D:
        D[data[3]] += int(data[2])
    else:
        D[data[3]] = int(data[2])

for key in sorted(D) : print (key,  D[key])
