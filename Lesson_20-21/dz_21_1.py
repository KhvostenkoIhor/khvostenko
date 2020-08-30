
class Car():
	'''A simple model of car that describes the make, model, 
	year, engine volume, color and price of the car'''
	
	'''Available car colors'''
	colors = ['black', 'blue', 'red', 'green', 'white']
	
	'''Possible engine volumes and car's prices'''
	volumes = {1.6: 43800, 2.0: 47500, 3.0: 59800, 5.5: 71100}
	
	
	def __init__(self, make: str, model: str, year: int):
		'''Initializes the car description attributes'''
		self.make = make
		self.model = model
		self.year = year
		self.engine_volume = 1.6
		self.color = Car.colors[0].title()
		self.price = Car.volumes[self.engine_volume]
	
	def __str__(self):		
		'''Returns a neatly formatted description'''
		return f'''
{self.year} {self.make.title()} {self.model.title()}
Engine volume: {self.engine_volume}
Color: {self.color}
Price: {self.price}
		'''
	
	def engine_volume_choice(self):
		'''Offers to choose one of the available engine volumes. 
		Returns the received value'''
		while True:
			print('Available volumes: 1.6, 2.0, 3.0, 5.5 l')
			try:
				choice = float(input('Choose the volume of the engine: '))
			except ValueError:
				print('Enter correct volume!')
			else:
				if choice in Car.volumes.keys():
					self.engine_volume = choice
					break
				else:
					print('This engine volume is not available')
					break
		return self.engine_volume			
	
	def price_setting(self, new_volume = 0.0):
		'''Sets the price of the car depending on the 
		engine volume. Returns the price'''
		if new_volume != 0.0 and new_volume in Car.volumes.keys():
			self.price = Car.volumes[new_volume]
			return self.price
		else:
			self.price = Car.volumes[self.engine_volume]
			print(f'{new_volume} engine volume is not available')
			return self.price	
	
	@property
	def set_color(self):
		'''Returns the default color of car'''
		return Car.colors[self.color].title()
		
	@set_color.setter
	def set_color(self, value):
		'''Allows to set the desired color of the car'''
		self.color = Car.colors[value].title()
			
if __name__ == '__main__':
	
	my_car = Car('audi', 'a6', 2018)
	volume = my_car.engine_volume_choice()
	#my_car.price_setting(volume)
	#print(my_car)
	print(my_car.engine_volume)
	print(my_car.price)
	print(my_car.color)	
	print(my_car.price_setting(3.0))
	#my_car.set_color = 2
	print(my_car.color)
	
