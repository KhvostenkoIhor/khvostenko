from random import choice


class Car():
	
	COLORS = (
	(0, 'RED'),
	(1, "YELLOW"),
	(2, 'GREEN'),
	(3, 'BLUE'),
	)
	RED = 0
	YELLOW = 1
	GREEN = 2
	BLUE = 3
	def __init__(
		self, brand: str = '', 
		engine_volume: float = 0.0, 
		color: int = YELLOW, 
		price: float = 0.0,
		):
		
		self.brand = brand
		self.engine_volume = engine_volume
		self.color = color
		self.price = price

	def change_engine_volume(self, volume: float):
		try:
			self.engine_volume = float(volume)
		except ValueError as e:
			print('Error: please enter a number of float')
			#ev = input('Enter engine volume: ')
			#self.change_engine_volume(volume = ev)
						
	def __str__(self):
		return f'''
		brand: {self.brand} 
		engine_volume: {self.engine_volume}
		color: {Car.COLORS[self.color][1]}
		price: {self.price}
		'''

	def change_color(self, color: str):
		try:
			for index, car_color in Car.COLORS:
				if color == car_color:
					self.color = index
					break
			else:
				raise ValueError('Error: Enter correct color')
				#print('ERROR: Enter correct color')
		except ValueError as e:
			print(e)
			
	@property
	def car_color(self):
		return Car.COLORS[self.color][1]

	@car_color.setter
	def car_color(self, value):
		self.color = value
	
		
if __name__ == '__main__':
	renault = Car()
	engine_volume = input('Enter engine volume: ')
	renault.change_engine_volume(engine_volume)
	print(renault)
	color = input("Enter the color: ")
	renault.change_color(color)
	print(renault)
	print(renault.car_color)
	renault.car_color = 2
	print(renault.car_color)
