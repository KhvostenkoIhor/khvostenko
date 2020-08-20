
def reader(text, mode='r'):
    with open(text, mode) as f:
        lines = f.readlines()
    return lines

def longest_line(list_of_strings):
    ls = [elem.rstrip() for elem in list_of_strings]
    longest_string = ls[0]
    for elem in ls:
        if len(elem) > len(longest_string):
            longest_string = elem
    return len(longest_string)
    
if __name__ == '__main__':
    way = '/storage/emulated/0/qpython/'
    name = 'simp.txt'
    text = f'{way}{name}'
    lst = reader(text)
    s = longest_line(lst)
    print(f'Longest string length: {s}')