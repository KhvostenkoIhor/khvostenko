
def add_player(first_name, last_name, age):
    player = {
        'First name': first_name,
        'Last name': last_name,
        'Age': age,
        }       
    players.append(player)
    return players

def delete_player(last_name):
    for ind, player in enumerate(players):
        if player['Last name'] == last_name:
            deleted_player = players.pop(ind)
            return deleted_player
    return ('This player does not exist')

def find_player(last_name):
	for player in players:
		if player['Last name'] == last_name:
			return player
	return ('This player does not exist')

def change_player(last_name):
	for ind, player in enumerate(players):
		if player['Last name'] == last_name:
			new_first = input('Enter new first name: ')
			player['First name'] = new_first
			new_last = input('Enter new last name: ')
			player['Last name'] = new_last
			new_age = input('Enter new age: ')
			player['Age'] = new_age
			return player
	return ('This player does not exist')

def show_players():
	for element in players:
		for key, value in element.items():
			print(key, value, sep=': ')
		print()
		

players = []

add_player('aaa', 'bbb', 28)
add_player('www', 'eee', 35)
add_player('zzz', 'ccc', 23)

while True:
    print('\nWhat do you want to do?')
    print("""Enter:
    1 - to see all players\n 
    2 - to add new player\n
    3 - to delete player\n
    4 - to find player\n
    5 - to change player's info\n
    q - to quit\n"""
    )
    choice = input(' ')
    if choice == 'q':
        break
    elif choice == '1':
        show_players()
    elif choice == '2':
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        age = input('Enter age: ')
        add_player(first_name, last_name, age)
        show_players()
    elif choice == '3':
        last_name = input('Enter last name: ')
        print(delete_player(last_name))
    elif choice == '4':
        last_name = input('Enter last name: ')
        print(find_player(last_name))
    elif choice == '5':
        last_name = input('Enter last name: ')
        print(change_player(last_name))
    else:
        print('You entered something wrong!')
