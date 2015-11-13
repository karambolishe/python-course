#! coding: utf-8

import os
import time
import sys

# User can enter folder for 3 times else default
# Add question about report creation again, if yes -> ask dir, else quit
# Add filter for items, choose item with "a" in name
# Write data to file with context manager 

try:
    var = input("Enter dir:")
    items = os.listdir(var)
    assert (len(items)>0), "No Items"
    
except (WindowsError,SyntaxError) as e :
    items = os.listdir("../..")
    print "Dir set to default!", e
else:
    print "Set "+var
finally:
    print "Next Step"
    
if __name__  == "__main__":
        
    header_line = "%.2s\t%25.25s\t%.10s\t%.25s"% tuple("# ITEM TYPE CREATION_TIME".split())
    print header_line
    count=1

    var_file = open('report.txt','a+')

    for item in items:
        
        date = time.ctime(os.path.getctime('../../'+item))
        if os.path.isdir('../../'+item):
            item_type = "<DIR>"
        else:
            item_type = "<File>"
        line = "%s  %30.40s\t%.10s\t%.25s"%(count,item,item_type,date)
        print line
        var_file.write(line+'\n')
        var_file.flush()
        count+=1

    var_file.close()
