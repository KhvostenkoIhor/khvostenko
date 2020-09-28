

class Stack():
    def __init__(self):
        self.stack = ['a', 'rtyy']
        self.lenght = 3

    def try_method(method):
        def wrapper(self, *string):
            try:
                method(self, *string)
            except Exception as e:
                print(f"You can't do that because {e}")
        return wrapper
       
    def stack_is_full(self):
        if len(self.stack) < self.lenght:
            return False
        return True
        
    def stack_is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    @try_method
    def add(self, string):
        if not self.stack_is_full():
            self.stack.append(string)
        else:
            raise Exception('Stack is full!')
            
    @try_method
    def delete(self):
        if not self.stack_is_empty():
            a = self.stack.pop()
            return a
        else:
            raise Exception('Stack is empty!')

    def clear_stack(self):
        if not self.stack_is_empty():
            self.stack = []
            return self.stack
            
    @try_method
    def show_last_string(self):
        if not self.stack_is_empty():
            print(f'The last string is "{self.stack[-1]}"')
            return self.stack[-1]
        else:
            raise Exception('Stack is empty!')
    
    def size(self):
        return len(self.stack)
        
    @property
    def stack_size(self):
        return self.lenght
        
    @stack_size.setter
    def set_size(self, value):
        self.lenght = value
       
if __name__ == '__main__':
    st_1 = Stack()
    while True:
        print('\nWhat to do?')
        answ = input('''Enter
"q" to quit
1 to add string to stack
2 to delete the last string from stack
3 to show the last string
4 to check the stack size
5 to check if the stack is empty
6 to check if the stack is full
7 to change the stack size  	
8 to clear the stack        	
''')    
        if answ == 'q' or answ == '':
            break
        elif answ == '1':
            string = input('Enter something: ')
            st_1.add(string)
        elif answ == '2':
            st_1.delete()
        elif answ == '3':
            st_1.show_last_string()
        elif answ == '4':
            print(f'The stack size is {st_1.size()}')
        elif answ == '5':
            if st_1.stack_is_empty():
                print('Stack is empty')
            else:
                print('Stack is not empty')
        elif answ == '6':
            if st_1.stack_is_full():
                print('Stack is full')
            else:
                print('Stack is not full')
        elif answ == '7':
            while True:
                a = input('Enter the new stack size: ')
                try:
                    a = int(a)
                    break
                except ValueError:
                    print('Incorrect value!')
            st_1.set_size = a
        elif answ == '8':
            st_1.clear_stack()


