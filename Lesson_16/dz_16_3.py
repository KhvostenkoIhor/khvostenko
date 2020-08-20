
def add():
    first = 'qwe' #input('Enter first name: ')
    last = 'rty' #input('Enter last name: ')
    numb = 23445 #input('Enter phone number: ')
    namer = first[:3]+last

    workers[namer] = {}
    workers[namer]['first name'] = first
    workers[namer]['last name'] = last
    workers[namer]['phone number'] = numb

def delete(last):
    for worker, info in workers.items():
        if info['last name'] == last:
            tmp_worker = workers.pop(worker)
            return tmp_worker
            break
        else:
            print('Worker ' + last + ' does not exist')

def search(last):
    for worker, info in workers.items():
        if info['last name'] == last:
            print('Nickname: ' + worker)
            for elem, value in info.items():
                print(elem, value, sep=': ')
            return {worker: info}
        else:
            print('Worker ' + last + ' does not exist')

def change(last):
    for worker, info in workers.items():
        if info['last name'] == last:
            new_first = '1111' #input('Enter new first name: ')
            new_last = '222' #input('Enter new last name: ')
            new_numb = '333' #input('Enter new phone number: ')
            


workers = {} 
add()
print(workers, '\n__________')
#worker = delete('ry')
#print(worker)
#print(workers)
ss = search('rty')
print('\n'*2, ss)
change('rty')


