class base:
	def __init__(self):
		print('base __init__')

class child1(base):
	def __init__(self):
		base.__init__(self)
		print('child1 __init__')

class child2(base):
	def __init__(self):
		base.__init__(self)
		print('child2 __init__')

class child3(child1,child2):
	def __init__(self):
		child1.__init__(self)
		child2.__init__(self)
		print('child3 __init__')

obj=child3()

print('-'*70)

class base:
	def __init__(self):
		print('base __init__')

class child1(base):
	def __init__(self):
		super().__init__()
		print('child1 __init__')

class child2(base):
	def __init__(self):
		super().__init__()
		print('child2 __init__')

class child3(child1,child2):
	def __init__(self):
		super().__init__()
		print('child3 __init__')

obj2=child3()