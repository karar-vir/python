n=int(input('enter 1st number and it should be small then 2nd number: '))
m=int(input('enter 2nd number and it should be greater than 1st number: '))

total=0
count=0
avg=0
'''
if n==m:
    total=n+m
    avg=total/2
else:    
    for i in range(n,m+1):
        total=total+i
        count=count+1
        #print(count)
    avg=total/count

print('Total={}  Average={}'.format(total,avg))
'''

if m==n:
    total=m+n
    avg=total/2
else:
    while n<=m:
        total=total+n
        count+=1
        n+=1
    avg=total/count
print('Total={} and Average={}'.format(total,avg))
