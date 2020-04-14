class Snake:
	name="Python"
	def change_name(self,new_name):
		self.name=new_name
snake=Snake()
print(snake.name)
snake.change_name("Anaconda")
print(snake.name)