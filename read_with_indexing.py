#open file with indexing
f=open('text.txt','r')
call=f.read()  #we can also use the 'readlines()' funtion
for lines in call:
   # print(call,end='')  #it will print the file of no. of lines
    print(lines,end='') #it will print the no of lines 
f.close()
