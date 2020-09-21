
import os

way = '/storage/emulated/0/qpython/Testing'

def get_files(way):
    for element in os.walk(way):
        for file in element[2]:
            if file.endswith('.py'):
                try:
                    with open(os.path.join(way, file), 'r') as f:
                        yield f
                except FileNotFoundError:
                    print(f'Wrong way for {file}')

#for i in get_files(way):
#    print(i)

def get_lines(way):
    for file in get_files(way):
        for line in file:
            yield line

#for i in get_lines(way):
#    print(i, end='')

def search_string(way, string):
    for line in get_lines(way):
        if string in line:
            yield line
            
string = 'while'
for i in search_string(way, string):
    print(i)            







