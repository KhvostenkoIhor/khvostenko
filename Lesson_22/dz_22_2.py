

class Ship():
	def __init__(self, name: str, displacement: int, country: str):
		self.ship_name = name.title()
		self.displacement = displacement
		self.country = country.title()
		self.gun_mount = 0
		self.rocket_launcher = 0
		self.torpedo_launcher = 0
		self.cannon = 0
		
	def set_weapons(self):
		gun_mount = 2 #input('Enter the number of gun mounts: ')
		if gun_mount :
			self.gun_mount = gun_mount
		rockets = 4 #input('Enter the number of rocket launchers: ')
		if rockets:
			self.rocket_launcher = rockets		
		torpedo = 2 #input('Enter the number of torpedo launchers: ')
		if torpedo:
			self.torpedo_launcher = torpedo
		cannons = 1 #input('Enter the number of cannons: ')
		if cannons:
			self.cannon = cannons

	def set_tasks(self):
		tasks = []
		while True:
			print('Enter "q" to qiut')
			task = input('Define the task of the vessel:\n')
			if task == 'q':
				break
			else:
				tasks.append(task)
		return tasks
			
	def __str__(self):
		return f'''
Ship name: {self.ship_name}
Displacement: {self.displacement} tons
Home country: {self.country}
Weapons: 
	Gun mounts - {self.gun_mount}
	Rocket launchers - {self.rocket_launcher}
	Torpedo launchers - {self.torpedo_launcher}
	Cannons - {self.cannon}
	'''		

class Frigate(Ship):
	def __init__(self, name, displacement, country):
		super().__init__(name, displacement, country)
		self.frig = self.set_tasks()
		self.weapons = {}
	
	def set_additional_weapons(self):
		while True:
			print('Enter "q" to stop adding weapons')
			key = input('Enter the weapon name: ')
			if key == 'q' or key == '':
				break
			value = input(f'Enter the number of {key.title()}: ')
			if value == 'q' or value == '':
				break
			self.weapons[key.title()] = value
		return self.weapons

	def show_info(self):
		print(self)
		print('Additional weapons:')
		for elem, value in self.weapons.items():
			print(' '*8, end='')
			print(elem, value, sep=' - ')
		print()
		print('Vessel tasks:')
		for task in self.frig:
			print(' '*8, end='')
			print(task)
		print()
			
class Destroyer(Ship):
	def __init__(self, name, displacement, country):
		super().__init__(name, displacement, country)
		self.frig = self.set_tasks()
		self.weapons = {}
	
	def set_additional_weapons(self):
		while True:
			print('Enter "q" to stop adding weapons')
			key = input('Enter the weapon name: ')
			if key == 'q' or key == '':
				break
			value = input(f'Enter the number of {key.title()}: ')
			if value == 'q' or value == '':
				break
			self.weapons[key.title()] = value
		return self.weapons

	def show_info(self):
		print(self)
		print('Additional weapons:')
		for elem, value in self.weapons.items():
			print(' '*8, end='')
			print(elem, value, sep=' - ')
		print()
		print('Vessel tasks:')
		for task in self.frig:
			print(' '*8, end='')
			print(task)
		print()
	
class Cruiser(Ship):
	def __init__(self, name, displacement, country):
		super().__init__(name, displacement, country)
		self.frig = self.set_tasks()
		self.weapons = {}
	
	def set_additional_weapons(self):
		while True:
			print('Enter "q" to stop adding weapons')
			key = input('Enter the weapon name: ')
			if key == 'q' or key == '':
				break
			value = input(f'Enter the number of {key.title()}: ')
			if value == 'q' or value == '':
				break
			self.weapons[key.title()] = value
		return self.weapons

	def show_info(self):
		print(self)
		print('Additional weapons:')
		for elem, value in self.weapons.items():
			print(' '*8, end='')
			print(elem, value, sep=' - ')
		print()
		print('Vessel tasks:')
		for task in self.frig:
			print(' '*8, end='')
			print(task)
		print()
		
if __name__ == '__main__':
	
	name = input('Enter the name of ship:')
	displacement = int(input("Enter the displacement of the vessel: "))
	country = input('Enter the home country of the ship: ')
	if 3000 <= displacement < 6000:
		ship = Frigate(name, displacement, country)
	elif 6000 <= displacement < 10000:
		ship = Destroyer(name, displacement, country)
	elif 10000 <= displacement < 20000:
		ship = Cruiser(name, displacement, country)
	else:
		print('You entered something wrong! Try again...')
	ship.set_weapons()
	ship.set_additional_weapons()
	ship.show_info()
