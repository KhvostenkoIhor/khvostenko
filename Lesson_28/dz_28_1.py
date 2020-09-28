
stack = [1, 3, 5, 8, 3]

def show_stack():
    print(f'Stack: {stack}')

def approve_number(num) -> bool:
    if num not in stack:
        return True

def approve(question):
    if question == add:
        app = input('Do you want to add it? y/n: ')
    else:
        app = input('Apply this operation for all numbers? y/n: ')
    return app

def add(num):
    if approve_number(num):
        stack.append(num)
    elif approve(add) == 'y':
        stack.append(num)

def get_number():
    while True:
        num = input('Enter the number: ')
        try:
            num = int(num)
            return num
            break
        except ValueError:
            print('You entered something wrong! Try again')

def number_counter(num):
    count = stack.count(num)
    return count

def edit_number(num_1, num_2):
    if number_counter(num_1) > 1 and approve(edit_number) == 'y':
        for ind, elem in enumerate(stack):
            if elem == num_1:
                stack[ind] = num_2
    else:
        stack[stack.index(num_1)] = num_2
    return num_2

def delete_number(num):
    if number_counter(num) > 1 and approve(delete_number) == 'y':
        for ind, elem in enumerate(stack):
            if elem == num:
                del stack[ind]
    else:
        del stack[stack.index(num)]
        
def is_number_in_stack(num):
    ind_lst = []
    for ind, elem in enumerate(stack):
        if elem == num:
            ind_lst.append(ind)
    return ind_lst

if __name__ == '__main__':
    while True:
        print('\nWhat to do?')
        print('''Enter 
 1 to add new number
 2 to edit some number
 3 to delete some number
 4 to find number 
 0 to show the stack
 "q" to quit''')
        choice = input('Make your choice: ')
        if choice == 'q':
            break
        elif choice == '1':
            add(get_number())
            print()
        elif choice == '0':
            show_stack()
            print()
        elif choice == '2':
            print('Searching')
            num_1 = get_number()
            if approve_number(num_1):
                print(f'Number {num_1} is not in stack')
            else:    
                print('Change to')
                num_2 = get_number()
                edit_number(num_1, num_2)
                print()
        elif choice == '3':
            num = get_number()
            if approve_number(num):
                print(f'Number {num} is not in stack')
            else:
                delete_number(num)
                print()
        elif choice == '4':
            num = get_number()
            if approve_number(num):
                print(f'Number {num} is not in stack')
            else:
                print(f'Number {num} is in such positions:')
                print(is_number_in_stack(num))
        else:
            print('You entered something wrong! Try again')
                
           




