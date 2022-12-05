open('testing.txt','r')
import os as o
if o.path.exists('testing.txt'):
    try:
        f=open('testing.txt','r')
        print('file is opened')
        if  f.closed==False:
            print('plz close the file')
        else:
            print('file is closed')
    except IOError:
        print('file is already opened')

else:
    print('file does not exist')
