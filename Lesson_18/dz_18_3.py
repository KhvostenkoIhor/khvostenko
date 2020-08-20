
def decor(func):
    def wrap(text, mode):
        global f
        with open(text, mode) as f:
            action = func(text)
        return action      
    return wrap

@decor
def reader(text):
    result = f.readlines()
    return result

@decor
def writer(new_file_name):
    f.write(new_text)

if __name__ == '__main__':
    way = '/storage/emulated/0/qpython/DZ_18/'
    name = 'simp.txt'
    file_ = f'{way}{name}'
    new_way = '/storage/emulated/0/qpython/'
    new_name = 'new_file.txt'
    new_file_ = f'{new_way}{new_name}'
    lines = reader(file_, 'r')
    del lines[-1]
    new_text = (''.join(lines))
    writer(new_file_, 'w')
