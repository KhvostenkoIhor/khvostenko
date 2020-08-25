from contextlib import contextmanager

@contextmanager
def doing_something():
    print('--> Start doing something...')
    yield
    print('<-- ...Stop doing something!')

with doing_something():
    print('...Process...')

@contextmanager
def open_file(file_name, mode):
    file_obj = open(file_name, mode)
    yield file_obj
    file_obj.close()

way = '/storage/emulated/0/qpython/DZ_19/'
name = 'simp1.txt'
file_name = f'{way}{name}'
file_name = 'simp.txt'

with open_file(file_name, 'w') as f:
    f.write('Hello Python World')

with open_file(file_name, 'r') as f:
	print(f.read())
