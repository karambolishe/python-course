__author__ = 'm.novikov'
putYear = int(input())

if putYear % 4 and putYear % 100 != 0 or putYear % 400 == 0:
    print('vysokos')
else:
    print('Year is not vysokos')

