#append 'a' will create a new file if the file does not exist
import os
appendfile=open('appendfile.txt','a')
appendfile.write('append will create a new file ')
appendfile.close()
os.remove('appendfile.txt')     #it will delete the file from the directory
