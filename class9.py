class student:
	def __init__(self,first,last,marks):
		self.first=first
		self.last=last
		self.marks=marks

	def myfun(self):

		return "Hello Mr." +'{} {}'.format(self.first,self.last)

	def per(self):
		self.marks=int(self.marks*1.05)


class stud(student):
	pass


obj=student('Karan','singh',70)
obj2=stud('King','Singh',390)
print(obj2.first)

print(obj.__dict__)			#it will return the data in dictionary 