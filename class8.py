class student:
	def __init__(self,first,last,marks):
		self.first=first
		self.last=last
		self.marks=marks

	def myfun(self):

		return "Hello Mr." +'{} {}'.format(self.first,self.last)

	def per(self):
		self.marks=int(self.marks*1.05)


obj=student('Karan','singh',70)

obj2=student('Param','singh',80)

print(obj.first, obj.last,obj.marks)

print(obj2.first,obj2.last,obj2.marks)

print(obj.myfun())

print(obj.first,obj.last,obj.marks)

obj.per()

print(obj.marks)

print(obj.per())		#why it will return None when i put inside the print() funtion