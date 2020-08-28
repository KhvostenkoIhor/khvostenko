
#class MyClass:
#	a = 10
#	b = 12
	
#	def __init__(self):
#		self.a = 99
		
#	def foo(self):
#		print('FOO', self.a)
		
		
#	def bar():
#		print('BAR', MyClass.a)

#if __name__ == '__main__':
	
#	ob_1 = MyClass()
#	ob_2 = MyClass()
	
#	ob_1.foo()
#	ob_2.foo()
	
#	MyClass.bar()
#	print(MyClass.a)
#	print(ob_2.a)
#	print(ob_2.b)
#	print(MyClass.a)
#	print(MyClass.b)
#	print(ob_1.foo)
#	print(MyClass.foo(ob_1))

#_____________________________________________________#


#class Temperature:
#	kelvins = 0
	
#	def __init__(self, celcius = 0):
#		self.celcius = celcius
#		self.kelvins = celcius + 273
	
#	def set_celcius(self, kelvins):
#		self.celcius = kelvins + 273
#		self.kelvins = kelvins

#	def set_kelvins(self, celcius):
#		self.kelvins = celcius + 273
#		self.celcius = celcius
		

#if __name__ == '__main__':
#	t = Temperature(25)
#	print(t.celcius)
#	print(t.kelvins)
#	t.set_kelvins(10)
#	print(t.celcius)
#	print(t.kelvins)
#	t.set_celcius(177)
#	print(t.celcius)
#	print(t.kelvins)


#_________________________________________________#

#class Temp:
#	def __init__(self, *, cels = 0):
#		self.cels = cels
	
#	@property	
#	def kelvin(self):
#		return self.cels + 273
	
#	@kelvin.setter
#	def kelvin(self, value):
#		self.cels = value - 273

#	@kelvin.deleter
#	def kelvin(self):
#		print('DELETED')
#		del self.cels
		
#if __name__ == '__main__':
#	t = Temp()
#	print(t.cels)
#	print(t.kelvin)
#	t.kelvin = 10
#	print(t.cels)
#	print(t.kelvin)
#	t.cels = 177
#	print(t.cels)
#	print(t.kelvin)
#	print(t.kelvin)
#	del t.kelvin
#	t.cels


#__________________________________________________#

#class Robot:
#	'''Этот класс представляет робота 
#	для уборки с именем '''
	
#	'''Переменная классаб которая содержит
#	количество роботов в целом'''
#	population = 0
	
#	def __init__(self, name):
#		'''Инициализация данных'''
#		self.name = name
#		print(f'Инициализация робота {self.name}')
		
		#При создании робота увеличиваем общее количество на 1
#		Robot.population += 1
		
#	def __del__(self):
#		'''Вызов деструктора когда удаляется объект робота'''
#		Robot.population -= 1
#		print(f'Робот {self.name} помер!')
#		
#		if Robot.population == 0:
#			print('Вы уничтожили всех роботов')
#		else:
#			print(f'Осталось {Robot.population} роботов')
			
#	def say_hi(self):
#		'''Приветствие отдельного робота'''
#		print(f"Привет, меня зовут {self.name}")
		
#	def how_many():
#		'''Выводит количество роботов'''
#		print(f'У нас здесь {Robot.population} роботов')


#if __name__ == '__main__':
#	droid_1 = Robot('R2-D2')
#	droid_2 = Robot('Walley')
#	del droid_1
#	Robot.how_many()
#	del droid_2
#	Robot.how_many()
#	print(Robot.__doc__)
#	print(dir(Robot))
#	print(Robot.__class__)	
#	wallie = Robot('Wallie')
#	r2d2 = Robot('R2-D2')
#	print(type(wallie))
#	print(type(5))

#____________________________________________#
class Robot:
	
	def __init__(self, name = ''):
		self.name = name
	
	def __str__(self):
		return f'My name is {self.name}'
		
	def __eq__(obj1, obj2): #сравнение
		#print(obj1)
		#print(obj2)
		return obj1.name == obj2.name

	def __add__(self, other): #добавление
		print(self)
		print(other)
		return [
			self,
			other
			]
	def __sub__(self, other): #отнимание
		if self.name > other.name:
			return self
		else:
			return other 
			
	def __div__(self, other): #деление без остачи
		pass
		
	def __

if __name__ == '__main__':
#	a = 10
#	b = 5
#	c = a - b	
	wallie = Robot('Wallie')
	wallie2 = Robot('Wallie 2')
	r2d2 = Robot('R2-D2')		
#	print(wallie)
#	print(r2d2)
#	print(dir(Robot))
#	print(c)
	robot_c = wallie == r2d2	#__eq__
	robot_c = wallie + r2d2		#__add__
	robot_c = wallie - r2d2		#__sub__
	robot_c = wallie / r2d2		#__div__
	
	print(ord('W'))
	print(ord('R'))
	print(robot_c)	
#____________________________________________________#










