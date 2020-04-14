import os
#Append mode is working in this file
#below block is creating a new txt file 
f=open('mysecondfile.txt','w')
f.write('hey Kannu your mekku is calling you\n')
f.close()

#below block is appending 'Today mekku is an in marriage Kannu !' at the end of "hey kannu your mekku is calling you\n"
#append 'a' will create a new file if the file will does not exist
f=open('mysecondfile.txt','a')
f.write('Today mekku is in marriage Kannu !')
f.close()

#below block is rewrite the 'mysecondfile.txt' and inside it "hello kannu existing data erased"
f=open('mysecondfile.txt','w')
f.write('hello Kannu your existing data erased')
f.close()

os.remove('mysecondfile.txt')       #it will delete the file from the directory
