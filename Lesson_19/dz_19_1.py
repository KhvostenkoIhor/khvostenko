
def add(dct):
    '''Adding new info about country'''
    country = input('Enter new country: ').title()
    capital = input('Enter the capital of new country: ').title()
    dct[country] = capital
    return dct
    
def delete(dct, key):
    '''Deleting info about country'''
    if key in dct.keys():
        tmp_key = {key: dct.pop(key.title())}
        return tmp_key
    else:
        return (f'Country {key.title()} does not exist!')

def search(dct, key):
    '''Searches the info about the country'''
    if key in dct.keys():
        searching = {key: dct[key].title()} 
        return(searching) 
    else:
        return (f'Country {key.title()} does not exist!')

def change(dct, key):
    '''Changing some info about the country'''
    if key in dct.keys():
        new_key = input('Enter new country name: ').title()
        if new_key:
            new_capital = input('Enter the name of capital: ').title()
            if new_capital:
                dct[new_key] = new_capital
                new_info = {new_key: dct[new_key]}
            else:
                dct[new_key] = dct[key].title()
                new_info = {new_key: dct[key].title()}
            del dct[key]
            return new_info
        else:
            dct[key] = input('Enter the capital of country: ').title()
            new_info = {key: dct[key].title()}
            return new_info
    else:
        return (f'Country {key.title()} does not exist!') 

def show_countries(dct):
    '''Shows the info about all countries in list'''
    print('Country: Capital')
    for key, value in sorted(dct.items()):
        print(key, value, sep=': ')

def saver(dct, file_):
    '''Pickling'''
    import pickle
    with open(file_, mode='wb') as f:
        pickle.dump(dct, f)
        
def loader(file_):
    '''Unpickling'''
    import pickle
    with open(file_, mode='rb') as f:
        dct = pickle.load(f)
    return dct
    
if __name__ == '__main__':
    countries = {
    	'Ukraine': 'Kyiv', 
    'Spain': 'Madrid', 
    'USA': 'Washington',
    }
    way = '/storage/emulated/0/qpython/DZ_19/'
    name = 'new_dct.bin'
    file_ = f'{way}{name}'
    
    while True:
        print('\nWhat do you want to do?')
        print('''Enter:
        1 - to see all countries in list\n 
        2 - to add new country\n
        3 - to delete country\n
        4 - to find country\n
        5 - to change some information\n
        6 - to save changes in the file\n
        7 - to load the the file\n
        q - to quit\n'''
        )
        choice = input(' ')
        if choice == 'q':
            break
        elif choice == '1':
            show_countries(countries)
        elif choice == '2':
            add(countries)
        elif choice == '3':
            key = input('Enter the name of country: ').title()
            print(delete(countries, key))
        elif choice == '4':
            key = input('Enter the name of searching country: ').title()
            print(search(countries, key))
        elif choice == '5':
            key = input('Enter the name of country to change info: ').title()
            print(change(countries, key))
        elif choice == '6':
            saver(countries, file_)
        elif choice == '7':
            print(loader(file_))        
        else:
            print('You entered something wrong!')
   






        