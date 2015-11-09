#! coding: utf-8
import os
import re
import glob
import matplotlib.pyplot as plt

__author__ = "s.tischenko"

os.chdir('..') # go to directory up

print 'Geting results from -', os.path.abspath('.') # print path current position
lst_files = glob.glob('*/test1*.txt')               # find exist files like the pattern
cmp = re.compile('Вопрос (\d{1,2}):(.*)',re.U)      # create object with number question and her answer like unicod text
test_dict = {'Answers':{}}                          # create dictionary and include dict

def check_test1(test_path):                         # create func with one param
    with open('s.tischenko/test.txt') as f:         # create object file as f (save method)
        for line in f.xreadlines():                 # begin iteration of every f.string
            key,value = cmp.search(line).groups()       # create variables key and values by using object cmp
            test_dict[key] = value.replace(',',' ').split() # add keys and values to dict
            
    with open(test_path) as f:                      # create object file as f (save method)
        with open(os.path.dirname(test_path)+'/result.txt','w') as fr:  #open file with write mode(use relative path)
            count = 17
            print test_path
            for line in f.xreadlines():             # handling every string file
                try:                                # handling exeptions
                    key,value = cmp.search(line).groups()   # using object cmp get key and value.
                except:
                    continue
                for v in test_dict[key]:
                    if v in value:
                        flag = 'True'
                    else:
                        flag = 'False'
                        count-=1
                        break
                    
                if flag=='True':
                    test_dict['Answers'][int(key)] = test_dict['Answers'].setdefault(int(key),0)+1
                else:
                    test_dict['Answers'].setdefault(int(key),0)
                    
                
                print 'Answer {0} - {1}'.format(key,flag)
                fr.write('Answer {0} - {1}\n'.format(key,flag))
            fr.write('{0} from {1}'.format(count,17))
            
def plot_creation(data):
    x = sorted(data)
    y = [data[key] for key in x]
    print x
    print y
    ymin = 0
    ymax = 25
    plt.xlabel('Question')
    plt.ylabel('Right Answers')
    plt.title('PYTHON TEST RESULTS')
    plt.xticks(x, x, size='small')
    plt.yticks(range(1,ymax), range(1,ymax), size='small')
    axes = plt.gca()
    axes.set_ylim([ymin,ymax])
    plt.plot(x, y, "go-", lw=2.0, label='1-st Test')
    for i,j in zip(x,y):
        plt.annotate(' %s/%s'%(str(y[i-1]),len(lst_files)), xy=(i,j+1),fontsize = 10,rotation=10 )
    plt.legend(loc='upper right', fontsize='medium', fancybox=True, shadow=True)
    plt.grid(True, which='both')
    Fig = plt.gcf()
    DefaultSize = Fig.get_size_inches()
    Fig.set_size_inches((DefaultSize[0]*1.5, DefaultSize[1]*1))
    Fig.savefig('python_test1.png')
    plt.show()
    #plt.close()
        
[check_test1(path) for path in lst_files]
plot_creation(test_dict['Answers'])
print sorted(test_dict['Answers'].items())
    
    
    
    
    
