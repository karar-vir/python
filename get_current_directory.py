#check the current directory
import os
os.getcwd()

f=open('text.txt','w')
list=('karanvir','singh ','I am last year student of Engineering')
f.writelines(list)      #list is passing with 'writelines()' only not work with write()
f.close()
