a = 'text'
b = 'Some more text 10'
c = 26

for i in (a, b):
    c = str(c)
    if c in i:
        print('String',c, 'True')

c = int(c)

if 0 < c < 25:
    print('In range')
elif c < 0:
    print('c < 0')
else:
    print('c > 25')