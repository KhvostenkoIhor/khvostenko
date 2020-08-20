
def add_word():
    new_word = input('Enter new word: ')
    translate = input('Enter the translation of new word: ')
    vocabulary[new_word] = translate
    return vocabulary
    
def delete_word():
    deleting_word = input('Enter the word you want to delete: ')
    for word, translation in vocabulary.items():
        if deleting_word in vocabulary.keys():        
            tmp_word = vocabulary.pop(deleting_word)
            return tmp_word
            break
        else:
            print('Word ' + str(deleting_word) + ' does not exist')
            break
    
def show_vocabulary():
    for word, translation in sorted(vocabulary.items()):
        print('Word: ' + str(word))
        print('Translation: ' + str(translation) + '\n')

def search_word():
    searching_word = input('Enter the word, you want to find: ')
    for word, translation in vocabulary.items():
        if searching_word in vocabulary.keys(): 
            print('Word: ' + str(searching_word))
            print('Translation: ' + str(vocabulary[searching_word]))
            break
        else:
            print('Word ' + str(searching_word) + ' does not exist')
            break

def change_word():
    change = input('Enter the word for changing translation: ')
    for word in vocabulary.keys():
        if change in vocabulary.keys():
            vocabulary[change] = input('Enter new translation for this word: ')
            break
        else:
            print('Word ' + str(change) + ' does not exist')
            break
            	
#if __name__ is '__main__':    
vocabulary = {'mother': 'mama', 'father': 'papa', 'sister': 'sestra', 'brother': 'brat'}

while True:
    print('\nWhat do you want to do?')
    print('''Enter:
    1 - to see all words in vocabulary\n 
    2 - to add new word\n
    3 - to delete some word\n
    4 - to find translation for some word\n
    5 - to change translation for some word\n
    q - to quit\n'''
    )
    choice = input(' ')
    if choice == 'q':
        break
    elif choice == '1':
        show_vocabulary()
    elif choice == '2':
        add_word()
        show_vocabulary()
    elif choice == '3':
        delete_word()
        show_vocabulary()
    elif choice == '4':
        search_word()
    elif choice == '5':
        change_word()
        show_vocabulary()
    else:
        print('You entered something wrong!')
