def cube(y):
    return y*y*y
d=lambda x:x*x*x
print(d(4))
print(cube(3))



li=[3,3,3,4,3,54,43,65,65,5,3,2,42]
final_lst=list(filter(lambda x:(x%2!=0),li))
print(final_lst)


final_lst2=list(map(lambda x:(x%2!=0),li))
print(final_lst2)

final_lst2=list(map(lambda x:x*x,li))
print(final_lst2)
