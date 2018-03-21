import sys
from panda import Series , DataFrame

file = open (r'E:\Python\Code\Data\DataText.txt', 'r')
#print (file.read())

#print (file.readline())

D={}

for line in open (r'E:\Python\Code\Data\DataText.txt', 'r'):
    words = line.rstrip().split(' ')
    for word in words:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1


S = Series(D)
print (S)
