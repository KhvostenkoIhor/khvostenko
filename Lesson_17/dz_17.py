
def task_1(text):
    '''Checks a string for palindromicity'''
    tmp_text = text.replace(' ', '').lower()
    if text and tmp_text[::-1] == tmp_text:
        return (text + ' is Palindrom!')
        #return True
    elif not text:
        return ('The string can not be empty!')
    else:
        return (text + ' is NOT Palindrom')
        #return False
    
def task_2(text):
    '''Searching reserved words in string and converts it to uppercase'''
    reserved_words = []
    print('Enter "q" to stop entering words')
    while True:
        word = input('Enter the woaaards, you want to reserve: ')        
        if word == 'q':
            break
        else:
            reserved_words.append(word)
    text = text.split()
    for i, el in enumerate(text):
        for j in reserved_words:
            if el.startswith(j):
                text[i] = el.upper()
    text = (' '.join(text))
    return text
    

def task_3(text):
    '''Counts the number of sentences in the text'''
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    return sentence_count

def show_result(foo):
    print(foo)
while True:
    print('\nWhat do you want to do?')
    answer = input('Enter:\n' +
        '1 - to check the text for palindromicity\n' +
        '2 - to search reserved words\n' +
        '3 - to count sentences\n' +
        'q - to quit\n'
        )
    if answer == 'q':
        break
    elif answer == '1':
        text = input('Enter the text:\n')
        show_result(task_1(text))
    elif answer == '2':
        text = input('Enter the text:\n')
        show_result(task_2(text))
    elif answer == '3':
        text = input('Enter the text:\n')
        show_result(task_3(text))
