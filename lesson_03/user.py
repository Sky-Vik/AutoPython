class User:
	
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def printFirstName(self):
		print(self.firstname)
	
	def printLastName(self):
		print(self.lastname)
	
	def printFullName(self):
		print(f"{self.firstname} {self.lastname}")