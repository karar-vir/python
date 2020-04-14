#print table of any number
for i in range(1,11):
    for  j in range(1,11):
        if(i%2==0):
            print('%d * %d = %d'%(i,i,i*j))
    print(end='\n')

