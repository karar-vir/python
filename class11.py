class base:
	def __init__(self):
		print('base __init__')

class child(base):
	def __init__(self):
		super().__init__()		# we can also use base.__init__(self):
		print('child __init__')
obj=base()
print('-'*20)
obj2=child()