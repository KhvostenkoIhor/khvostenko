
class Stadium():
	'''Describes some stadium in the world'''
	
	def __init__(self, name, open_date):
		'''Initializer'''
		self.name = name
		self.open_date = open_date
		self.country = ''
		self.city = ''
		self.stadium_capacity = 0
		
	def __str__(self):
		'''Returns the description of the stadium'''
		return f'''
	Stadium name: {self.name}
	Opening date: {self.open_date}
	Country: {self.country}
	City: {self.city}
	Stadium capacity: {self.stadium_capacity}
	'''
	
	@property
	def set_country(self):
		return self.country
		
	@set_country.setter
	def set_country(self, value):
		self.country = value.title()
	
	@property
	def set_city(self):
		return self.city
		
	@set_city.setter
	def set_city(self, value):
		self.city = value.title()
		
	@property
	def set_capacity(self):
		return self.stadium_capacity
		
	@set_capacity.setter
	def set_capacity(self, value):
		self.stadium_capacity = value
			
if __name__ == '__main__':
	
	name = 'Estadio Santiago Bernabeu' #input('Enter the name of the stadium: ')
	date = '14.12.1947' #input('Enter the opening date of the stadium: ')
	my_stad = Stadium(name, date)
	my_stad.set_country = 'spain' #input('Enter the country: ') 
	my_stad.set_city = 'madrid' #input('Enter the city: ')
	my_stad.set_capacity = 81044 #input('Enter the capacity of the stadium: ') 
	#print(my_stad.country)
	#print(my_stad.open_date)
	#print(my_stad.stadium_capacity)
	print(my_stad.set_capacity)
	my_stad.set_capacity = 10000
	print(my_stad.set_capacity)
	print(my_stad)

