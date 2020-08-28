#pack unpuck
#obj = struct.pack(format, v1, v2, v3) #.......)
#obj2 = struct.unpuck(format, buffer)
#struct.method(format)

#import struct
#print(dir(struct))
#ls = [1, 3, 9, 12, 14]
#obj = struct.pack('>5i', ls[0], ls[1], ls[2], ls[3], ls[4])

#size = struct.calcsize('<5i')
#print('obj: ', obj)
#print('size: ', size)

#параметры для format  @ = < > !
# @ - природный размер по умолчанию
# = стандартный - не выравнивается
# < > - little-endian  big endian сначала обрабатывается младший/старший байт

# i - integer
# q - long
# c - char
# s - char[]
# f - float
#______________________________________________________________________#

#import pickle

#работа с байтами
#dump
#load

#pickle.dump(obj, file, protocol=None, *, fix_imports=True)
#obj = pickle.load(file)

#my_list = [1, 2, 3, 4, 5]

#f = open('my_file.bin', 'wb')
#pickle.dump(my_list, f)
#f.close()
#f = open('my_file.bin', 'rb')
#my_object = pickle.load(f)
#print(my_object)

#def add_info(country: str, capital: str):
	#with my_serializer() as s:
#	pass
	
#def update_country(country: str):
#	pass

#db = open('db.sqlite3', 'rb')
#close()

###КОНТЕКСТНЫЕ МЕНЕДЖЕРЫ
##Менеджер open()
#f = open('f1.txt', 'r')
#text = f.readlines()
#print(text)
#f.close
#
#
#with open('f1.txt', 'r') as f:
#	text = f.readline()
#	print(text)

##СВОЙ МЕНЕДЖЕР##
#from contextlib import contextmanager
#import sqlite3

def global_try(func):
	def wrapper():
		try:
			func()
		except FileNotFoundError as e:
			print(f'Error: {e}')
		except Exseption as e:
			print(f'ERROR: {e}')
	return wrapper


#@contextmanager
#def read_file(file_name: str):
#	file = open(file_name, 'r')
	
#	try:
#		print(f'File {file_name} is opened')
#		yield file
#	finally:
#		file.close()
#		f = open(file_name, 'a')
#		f.write('Some text')
#		file.close()
#		print(f'File {file_name} is closed')
		
@global_try
def read_my_file():
	with open('my_file.txt') as f:
		a = f.readlines()
		print(a)


#	with read_file('my_file_3.txt') as f:
#		a = f.readlines()
#		print(a)

#read_my_file()	
#______________________________________________________________________#

###   ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ   ###

#sex:
#	MALE: True
#	FEMALE: False

#Person:
#	name: str
#	age: int
#	sex: bool
	
#dima = Person(
#	name: 'Dima',
#	age: 40,
#	sex: sex.MALE
#	)

#irina = Person(
#	name: 'Irina',
#	age: 22,
#	sex: sex.FEMALE
#	)

