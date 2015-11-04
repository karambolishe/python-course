#! coding: utf-8
import logging
import time

time.clock()
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.info('Start of program')

def func(a,b):
    x =[i for i in xrange(a,b) if i%2!=0 or i==2]
    value = {}
    for i in x:
        for j in xrange(1,i,2):
            logging.debug('%s // %s = %i.%s'%(i,j,i/j,i%j))
            if i%j==0:
                value.setdefault(i,[]).append(j)
            elif len(value[i])>1:
                break
    return [key for key in sorted(value.keys()) if len(value[key])==1]



#print func(2,10000)# => 7.82252530994 sec.

logging.info('End of program')

my_time = time.clock()
print 'my time --- ',my_time

def func2(m,n):
    a = [True] * n
    for i in xrange(2, n):
            for j in xrange(i * 2, n, i):
                    a[j] = False
    b = [i for i in xrange(2, n) if a[i] and i>m]
    return b

print func2(20,10000)

print time.clock() - my_time

'''
Для нахождения всех простых чисел не больше заданного числа n, следуя методу Эратосфена, нужно выполнить следующие шаги:

Выписать подряд все целые числа от двух до n (2, 3, 4, …, n).
Пусть переменная p изначально равна двум — первому простому числу.
Зачеркнуть в списке числа от 2p до n считая шагами по p (это будут числа кратные p: 2p, 3p, 4p, …).
Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.
Повторять шаги 3 и 4, пока возможно.
Теперь все незачёркнутые числа в списке — это все простые числа от 2 до n.
'''
