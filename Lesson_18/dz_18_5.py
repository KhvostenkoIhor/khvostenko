
def reader(text, mode='r'):
    '''Opening file for reading only'''
    with open(text, mode) as f:
        string = f.read()
    return string

def counter(string):
    '''Counts the number of occurrences
    of a given word'''
    count_of_word = string.count(word)
    return count_of_word


if __name__ == '__main__':
    way = '/storage/emulated/0/qpython/'
    name = 'simp.txt'
    file_ = f'{way}{name}'
    word = input('Enter the word: ')
    string = reader(file_)
    print(f'Count of word {word} is {counter(string)}')
