

def decor(func):
    '''Opening file for R/W operations'''
    def wrap(text, mode):
        global f
        with open(text, mode) as f:
            action = func(text)
        return action      
    return wrap

@decor
def reader(text):
    '''Opening file for reading'''
    result = f.read()
    return result

@decor
def writer(new_file_name):
    '''Writing new info to the file'''
    f.write(new_text)
    
def change(string):
    '''Searching for the specified word 
    and replace it with a new one'''
    if word in string:
        string = string.replace(word, changing)
    return string


if __name__ == '__main__':
    way = '/storage/emulated/0/qpython/'
    name = 'simp.txt'
    file_ = f'{way}{name}'
    word = input('Enter the word, you want to change: ')
    changing = input('Enter the word for change: ')
    string = reader(file_, 'r')
    new_text = change(string)
    writer(file_, 'w')
    
    
   


