li=[24,3,42,423,54,46,56,46,54,654,5,7,67]
print('id of before any function ',id(li),'original list is : ',li)
x=sorted(li)
print('id od li : ',id(x),'after sorted funtion list is : ',x)
li.sort()
print('after sort funtion list is : ',li)
