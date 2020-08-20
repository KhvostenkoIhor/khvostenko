

def reader(text, mode='r'):
    '''Opening file for reading'''
    with open(text, mode) as f_string:
        string = f_string.read()
    return string

def writer(info, new_file_name, mode='w'):
    '''Opening file for write'''
    with open(new_file_name, mode) as f_new:
        f_new.write(info)

def lines_reader(text, mode='r'):
    '''Opening file for reading lines'''
    with open(text, mode) as f_lines:
        lines = f_lines.readlines()
        number_of_lines = 0
        for line in lines:
            if line != '\n':
                number_of_lines += 1
    return number_of_lines

def number_of_chars(string):
    '''Returns the number of chars in the text'''
    return len(string)
    
def number_of_vowels(string):
    '''Counts the number of vowels in the text''' 
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'ы', 'о', 'у', 'э', 'ю', 'я']
    vowels = 0
    for letter in string:
        if letter in vowels_list:
            vowels +=1
    return vowels
    
def number_of_consonants(string):
    '''Counts the number of consonants in the text'''
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'ы', 'о', 'у', 'э', 'ю', 'я']
    consonants = 0
    for letter in string:
        if letter.isalpha() and letter not in vowels_list:
            consonants += 1
    return consonants
    
def number_of_digits(string):
    '''Counts the number of digits in the text'''
    digits = 0
    for letter in string:
        if letter.isdigit():
            digits += 1
    return digits

def analytics(file_name):
    '''Returns analytic information about the text'''
    string = reader(file_name)
    lines = (f'Number of lines: {lines_reader(file_name)}')
    chars = (f'Number of chars: {number_of_chars(string)}')
    vowels = (f'Number of vowels: {number_of_vowels(string)}')
    consonants = (f'Number of consonants: {number_of_consonants(string)}')
    digits = (f'Number of digits: {number_of_digits(string)}')
    return (lines, chars, vowels, consonants, digits)


if __name__ == '__main__':
    way = '/storage/emulated/0/qpython/'
    name = 'simp.txt'
    file_ = f'{way}{name}'
    info = ('\n'.join(analytics(file_)))
    writer(info, 'new_analytics.txt')
    for elem in analytics(file_):
        print(elem)