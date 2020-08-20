
def reader(text, mode='r'):
    '''Opening file for reading only'''
    with open(text, mode) as f:
        lines = f.readlines()
    return lines

def uniq_lines(lst_1, lst_2, list_of_uniq_lines):
    '''Searching for unique lines in lists of strings'''
    lst_1 = [line.rstrip() for line in lst_1]
    lst_2 = [line.rstrip() for line in lst_2]
    for line in lst_1:
        if line not in lst_2:
            list_of_uniq_lines.append(line)
        else:
            continue
    return list_of_uniq_lines   

if __name__ == '__main__':
    way_1 = '/storage/emulated/0/qpython/DZ_18/'
    way_2 = '/storage/emulated/0/qpython/'
    name = 'simp.txt'
    file_1 = f'{way_1}{name}'
    file_2 = f'{way_2}{name}'
    text_1 = reader(file_1)
    text_2 = reader(file_2)
    list_of_uniq_lines = []
    uniq_lines(text_1, text_2, list_of_uniq_lines)
    uniq_lines(text_2, text_1, list_of_uniq_lines)
    if len(list_of_uniq_lines) > 0:
        print('Unique lines:')
        for line in list_of_uniq_lines:
            print(line)
    else:
        print('No unique lines found!')
