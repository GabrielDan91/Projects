board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(board)

def welcome_tik():
    print("Welcome to the tik tak toe game\n"
          "The game must be played by two players\n"
          "Player1 must chose first the marker with which he will play\n"
          "After the election the game will start and the players must pick a number from the board where they want "
          "to put their marker\n"
          "The player ho has complete a line  with three markers, is the winner")
    print('\n'*2)

# welcome_tik()

def clear_output():
    print('\n'*5)

def board_print(b):
    clear_output()
    print('|' + b[7] + '|' + b[8] + '|' + b[9] + '|')
    print('|' + b[4] + '|' + b[5] + '|' + b[6] + '|')
    print('|' + b[1] + '|' + b[2] + '|' + b[3] + '|')

# board = board_print(board)

def choose_x_o():
   markers = ['X', 'O']
   while True:
       player1 = input("Please pick a marker 'X' or 'O': ").upper()
       if player1 not in markers:
           print("You must enter 'X' or 'O'")

       elif player1 == 'X':
           return ('X', 'O')

       else:
           return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

import random
def choose_first():
    player_chosen = random.randint(0, 1)
    if player_chosen == 0:
        return 'player1'
    else:
        return 'player2'

def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def pick_a_number(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):

        position = int(input('Please pick a number from the board who is not elected: '))

    return position



def replay():
    return  input("Play again? Enter Y/N: ").lower().startswith('y')


def tic_tac_toe():
    welcome_tik()
    while True:
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player1_marker, player2_marker = choose_x_o()

        turn = choose_first()
        print(turn + ' will go first')

        play_game = input("Ready to play? Y/N ").upper()
        if play_game == 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == "player1":
                # Show the board
                board_print(board)
                # Choose a position
                position = pick_a_number(board)
                # Place the marker on the position
                place_marker(board, player1_marker, position)
                # Check if they won
                if win_check(board, player1_marker):
                    board_print(board)
                    print("Player 1 has won!")
                    game_on = False

                else:
                    if full_board_check(board):
                        board_print(board)
                        print("Tie game")
                        break
                    else:
                        turn = "player2"
            else:
                if turn == "player2":
                    # Show the board
                    board_print(board)
                    # Choose a position
                    position = pick_a_number(board)
                    # Place the marker on the position
                    place_marker(board, player2_marker, position)
                    # Check if they won
                    if win_check(board, player2_marker):
                        board_print(board)
                        print("Player 2 has won!")
                        game_on = False

                    else:
                        if full_board_check(board):
                            board_print(board)
                            print("Tie game")
                            break
                        else:
                            turn = "player1"

        if not replay():
            break

tic_tac_toe()