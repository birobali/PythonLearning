def main():
    if input('Do you want to play Tic-tac-toe? (yes/no): ') == 'no':
        return

    players = initialize_players()
    play(players)


def play(players):
    display_board(help_standing())
    last_step = 'player2'
    standing = init_standing()
    while not is_somebody_won(standing):
        player_name = players['player1']['name'] if last_step == 'player2' else players['player2']['name']
        inp = int(input(f'{player_name}\'s turn. Please choose a field from 1-9: '))
        last_step = 'player1' if last_step == 'player2' else 'player2'
        standing[inp] = players[last_step]['sign']
        display_board(standing)
    else:
        print(f'Congratulation {players[last_step]["name"]} won!')
        if input('Do you want to play once more? (yes/no): ') == 'yes':
            play(players)


def help_standing():
    return {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def init_standing():
    return {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def is_somebody_won(standing):

    for signs in [['X', 'X', 'X'], ['O', 'O', 'O']]:
        if [standing[1], standing[2], standing[3]] == signs or [standing[4], standing[5], standing[6]] == signs or [standing[7], standing[8], standing[9]] == signs or [standing[1], standing[4], standing[7]] == signs or [standing[2], standing[5], standing[8]] == signs or [standing[3], standing[6], standing[9]] == signs or [standing[1], standing[5], standing[9]] == signs or [standing[3], standing[5], standing[7]] == signs:
            return True
    else:
        return False

def initialize_players():
    player = {'name': None, 'sign': None}
    players = {'player1': dict(player), 'player2': dict(player)}

    players['player1']['name'] = input('Player 1 what is your name? ')
    players['player1']['sign'] = input("Do you want to be 'X' or 'O'? ").upper()
    print(f'Thank you! \n Your name is {players["player1"]["name"]} and you are with: {players["player1"]["sign"]}')

    players['player2']['name'] = input('Player 2 what is your name? ')
    players['player2']['sign'] = 'X' if players['player1']['sign'] == 'O' else 'O'
    print(f'Thank you! \n Your name is {players["player2"]["name"]} and you are with: {players["player2"]["sign"]}')
    print(players['player1']['name'] + ' starts!')
    return players


def display_board(standing):
    print(f' {standing[1]} | {standing[2]} | {standing[3]} ')
    print('---|---|---')
    print(f' {standing[4]} | {standing[5]} | {standing[6]} ')
    print('---|---|---')
    print(f' {standing[7]} | {standing[8]} | {standing[9]} ')


main()
