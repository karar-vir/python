#we will remove the file from the directory
import os
namefile=open('openfile.txt','w')
namefile.write('hello your file is created')
namefile.close()
if os.path.exists('openfile.txt'):
    os.remove('openfile.txt')
else:
    print('your file not exits')
