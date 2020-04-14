#direct assingning tha value in multiple data types like dict,tuples, list etc.
lst=[]
lst[0]=1    #IndexError: list assignment index out of range
print(lst)

diction={}
diction[1]="apple"      #it will work becaues index assignment is directly we can give in dictionary
print(diction)
'''
tup=()
tup[0]="Lion"       #we can't assign the value to tuple because tuple is unordered and not supporting the indexing
print(tup)
'''
