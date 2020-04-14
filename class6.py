class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def myfun(self):
		print('Hello my name is '+self.name)
obj1=Person('Karan',24)
print(obj1.name)
print(obj1.age)
obj1.myfun()	#if i will put 'obj1.myfun()' inside the print statement then it will return None also with output