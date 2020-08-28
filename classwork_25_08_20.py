
##

players = []

#player = {
#	'name': str,
#	'surname': str,
#	'age': int,
#	}

#def get_players():
#	return players
	
#def add_player(name: str, surname: str, age: int):
#	player = {
#	'name': name,
#	'surname': surname,
#	'age': age,
#	}
#	players.append(player)

#def pprint(*args):
#	print('--------')
#	for i in args:
#		print(i)
#	print('---------')

#if __name__ == "__main__":
	
#	add_player(
#	name = 'Ilya',
#	surname = 'Ostapchenko',
#	age = 25)

#	fs = get_players()
#	pprint(fs)
	
##________ OOP _________###

#class Dog():
	#Attributes
#	total_count = 0
	
	#Initializer
#	def __init__(self, name: str, age: int):
#		Dog.total_count += 1
#		self.name = name
#		self.age = age
		
	#Methods
#	def say_wof(self):
#		print("-WOF-")
		
#	def say_name(self):
#		print(f'--WOF, my name is {self.name}')

#	def print_something():
#		print('biliberda')
		
#if __name__ == "__main__":
#	barbos = Dog('Barbos', 4)
#	tuzik = Dog('Tuzik', 7)
	
#	barbos.say_wof()
#	barbos.say_name()
#	
#	tuzik.say_wof()
#	tuzik.say_name()
#	
#	print(barbos.name)
#	print(tuzik.age)
#	
#	Dog.print_something()
#	Dog.say_name(tuzik)
#	Dog.say_name(Dog(name='DOOOG', age = 10))
	
#	dogs = Dog.total_count
#	dogs_2 = tuzik.total_count
#	print(dogs)
#	print(dogs_2)
	
#	print(barbos)
#	print(tuzik)
#	print(Dog)
from datetime import date
import random
	
class Car():
	
	def __init__(self, brand: str, model: str, year: int):
		self.brand = brand
		self.model = model
		self.year = year
		
	def set_engine_volume(self):
		self.volume = int(input('Enter the volume of engine: '))
		return self.volume
		
	def set_color(self):
		colors =['Red', 'Blue', 'Green',]
		self.color = random.choice(colors)
		return self.color
		
if __name__ == '__main__':
	my_car = Car('audi', 'a6', 2018)
	
	print(my_car.brand)
	print(my_car.model)
	print(my_car.year)
	
	my_car.set_engine_volume()
	print(my_car.volume)
	
	my_car.set_color()
	print(my_car.color)
	

		
		
					
		
		
		






















