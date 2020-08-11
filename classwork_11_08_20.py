# dct = {5: 'something'}
# print(dct)

# dct = {
#     1: 'hello',
#     'key_2': 'python',
#     345: '!!!',
# }
# print(dct)

# players = {}
# while True:

#     i = 0
#     namer = i + 1
#     name = 'player_' + namer + input("Enter ")
#     players[name] = input('Enter the name of player: ')
#     if players[name] == 'q':
#         break
    
# players = {}

# def add_player(f):
#     global players
#     players[key] = f

# def delete_player(f_key):
#     global players
#     del(players[f_key])

# def find_player(f_key):
#     global players
#     return players[f_key]

# def show_team(players):
#     for key, value in players.items():
#         print(key, ';', value)

# if __name__ == '__main__':
#     print('Enter ' +
#     1 - to add player +
#     2 - to delete player +
#     3 = to find player
#     )
# choice = int(input('What do you want to do?\n'))
# if choise == 1:
#     first = input('Enter the first name of player\n')
#     last = input('Enter the last name of player\n')
#     add_player(key, {'Name': first + " " + last})

# elif choice == 2:
#     pass

# elif choice == 3:
#     pass

# elif choice == 4:
#     pass

def get_players(players):
    return players

def print_result(*args):
    for el in args:
        print(el)
        input('Press to continue...')

def add_player(first_name, last_name, middle_name):
    global players
    player = {
        'First name': first_name,
        'Last name': last_name,
        'Middle name': middle_name,
    }
    players.append(player)
    return player

def del_player(last_name):
    global players
    for index, player in enumerate(players):
        if player['last_name'] = last_name:
            deleted_player = player
            del(players[index])
            return deleted_player

def update_player(last_name):
    global players

    for index, player in enumerate(players):
        if player['last_name'] = last_name:
            first_name = player['First name']
            last_name = player['Last name']
            middle_name = player['Middle name']
            new_first = input(f'Enter first name ({first_name} - default)')
            new_last = input(f'Enter first name ({last_name} - default)')
            new_middle = input(f'Enter first name ({middle_name} - default)')

            
            
            return

if __name__ == '__main__':
    
    players_list = 'list'
    add_player = 'add'
    delete_player = 'delete'
    update_player = 'update'
    search_player = 'search'
    exit = 'q'

    players = []

    while True:
        print(f'''
        Choices:
        list of players: 1
        add_player: 2
        delete_player: 3
        update_player: 4
        search_player: 5
        exit: q
        ''')
        choice = input('Enter choice:\n')
        if choice == exit:
            break
        elif choice == players_list:
            players = get_players(players)
            print_result()

        elif choice == add_player:
            first_name = input("Enter first name\n")
            last_name = input('Enter last name\n')
            middle_name = input('Enter middle name\n')

            player = add_player(
                first_name = first_name,
                last_name = last_name,
                middle_name = middle_name
            )
            print_result(players)

        elif choice == delete_player:
            last_name = input('Enter players last_name: ')
            player = del_player(last_name = last_name)
            print_result(player)

        elif choice == update_player:
            last_name = input('Enter last name: ')
            player = update_player(last_name = last_name)
            print_result(player)