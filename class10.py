class mammals:
	def __init__(self,mammal_name):
		print(mammal_name,'is a faithful animal')

class Dog(mammals):
	def __init__(self):
		print('Dog has four legs')
		super().__init__('Dog')

obj=Dog()
