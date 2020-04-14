#Abstract Class
#we can't create the  object directly of any abstract class,if we want to create the object of abstract class then before 
#we need to inherit that abstract into another class after that we can create it object othwise it will not possible
#**********Python can't be directly allow to abstract class but with the help of 'ABC'=='Abstract Base Class' module we can implement abstraction**************
#By default python can't allow to abstraction
from abc import ABC,abstractmethod

class computer(ABC):  #ABC is necessary to mention inside the computer funtion because it makes the computer as abstract class
	@abstractmethod
	def process(self):
		pass


class laptop(computer):
	pass

obj=laptop()
	

#above program will throw an error it is due to undefined class laptop if we will put somthing inside the laptop then it will work lets try below 

class computer1(ABC):
	@abstractmethod
	def process1(self):
		pass

class laptop1(computer1):
	def process1(self):
		print('inside process1')

obj=laptop1()
print(obj.process1)