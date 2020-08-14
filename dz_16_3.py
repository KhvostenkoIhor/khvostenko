
def add(dct):
    print('Adding a new worker:')
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    numb = input('Enter phone number: ')
    namer = first[:3]+last

    dct[namer] = {}
    dct[namer]['first name'] = first
    dct[namer]['last name'] = last
    dct[namer]['phone number'] = numb

def delete(dct, last):
    for worker, info in dct.items():
        if info['last name'] == last:
            tmp_worker = dct.pop(worker)
            return tmp_worker
            break
    else:
        print('Worker ' + last + ' does not exist')

def search(dct, last):
    for worker, info in dct.items():
        if info['last name'] == last:
            print('Nickname: ' + worker)
            for elem, value in info.items():
                print(elem, value, sep=': ')
            return {worker: info}
    else:
        print('Worker ' + last + ' does not exist')

def change(dct, last):
    for worker, info in dct.items():
        if info['last name'] == last:
            new_first = input('Enter new first name: ')
            new_last = input('Enter new last name: ')
            new_numb = input('Enter new phone number: ')
            if new_first:
                info['first name'] = new_first
            if new_last:
                info['last name'] = new_last
            if new_numb:
                info['phone number'] = new_numb
            namer = new_first[:3] + new_last
            new_worker = {namer: info}
            dct[namer] = info
            del(dct[worker])
            return new_worker
    else:
        print('Worker ' + last + ' does not exist')
            
def show_workers(dct):
    if dct:
        for worker, info in dct.items():
            print('Nickname: ' + worker)
            for elem, value in info.items():
                print(elem, value, sep=': ')
            print()
    else:
        print('Your dictionary is empty!')

if __name__ == '__main__':    
    workers = {
    	    'qwerty': {
            'first name': 'qwe',
            'last name': 'rty', 
            'phone number': 23455,
            }
        }

    while True:
        print('\nWhat do you want to do?')
        print('''Enter:
        1 - to see all workers\n 
        2 - to add new worker\n
        3 - to delete some worker\n
        4 - to find info of some worker\n
        5 - to change info of some worker\n
        q - to quit\n'''
        )
        choice = input(' ')
        if choice == 'q':
            break
        elif choice == '1':
            show_workers(workers)
        elif choice == '2':
            add(workers)
        elif choice == '3':
            last = input('Enter last name of worker: ')
            delete(workers, last)
        elif choice == '4':
            last = input('Enter last name of worker: ')
            search(workers, last)
        elif choice == '5':
            last = input('Enter last name of worker: ')
            change(workers, last)
        else:
            print('You entered something wrong!')
