class Person:

	def __init__(myobj1,name,age):
		myobj1.name=name
		myobj1.age=age
	def myfun(myobj):
		print('my name is '+myobj.name)

c1=Person('karan',23)
print(c1.name)
print(c1.age)
p1.age=45
print(p1)
c1.myfun()