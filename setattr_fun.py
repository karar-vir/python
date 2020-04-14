#setattr() funtion in python.
#we can't assign the setattr to any variable then if we print it will return None 
class test_getattr:
    name='karan'

obj=test_getattr()
print('before applying getattr :',obj.name)
setattr(obj,'name','Param')
print('applying after getattr : ',obj.name)
