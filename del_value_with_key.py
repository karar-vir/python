#delete the value with the del keyword and its key
#del dict-name [key] one thing always keep in mind del dict-name enclosed with squrae brackett [] not wiht pranthesis()

diction={'name':'karan'}
diction_update={'course':'B-Tech'}
diction.update(diction_update)
print(diction)
del diction['name']
print(diction)
