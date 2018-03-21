import sys
def countlines(name):
    return len(open(name,'r').readlines())

def countChars(name):
    return len(open(name,'r').read())

def test(name):
    print('No. of lines : ', countlines(name))
    print('No of Chars : ', countChars(name))

if (__name__ == '__main__'):
    if len(sys.argv) > 1 :
        test(sys.argv[1])
    elif input('want to Enter Filename:') == '1' :
        test(input('Entr filename:'))
    else:
        test('E:\\Python\\Data\\Data.txt')

