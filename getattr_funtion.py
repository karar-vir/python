#how we use getattr() function.we can only pass one item in the getattr()
class student:
    name='Karan'
    course='B-Tech'
    roll=12345
x=getattr(student,'name')
y=setattr(student,'roll',89588)
print(x)
print(y)


#output - Karan
