# inheritance.py
class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print ("Last name: "+self.last_name)
		print("Eye color: "+self.eye_color)

class Child(Parent):
	"""Child inherits from parent"""
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	def show_info(self): # method overriding
		print ("Last name: "+self.last_name)
		print("Eye color: "+self.eye_color)
		print("Number of toys: "+str(self.number_of_toys)) # str used for print of integer
		

bojana_perisic = Parent("Perisic", "brown")
# bojana_perisic.show_info()
# print(bojana_perisic.last_name)

lana_perisic = Child("Perisic", "blue", 132)
lana_perisic.show_info()
# print(lana_perisic.last_name)
# print(lana_perisic.number_of_toys)