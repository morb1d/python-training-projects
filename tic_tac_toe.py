board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1 = "X"
player2 = "O"
def print_board(game_board):
    for i, value in enumerate(game_board):
        if (i < 2 and i != 1):
            print(' %s ' %(value), end='')
        elif (i > 2 and i < 5 and i != 4):
            print(' %s ' %(value), end='')
        elif (i > 5 and i < 9 and i != 7):
            print(' %s ' %(value), end='')
        elif (i == 2 or i == 5 or i == 8):
            print(' %s ' %(value))
            if (i != 8):
                print("---|---|---")
        elif (i == 1 or i == 4 or i == 7):
             print('| %s |' %(value), end='')
        else:
            pass

def ask_for_input():
    print()
    player_input = int(input("Your choice? "))
    return player_input

def check_game_state(game_board):
    

board[ask_for_input()] = player1
print_board(board)
board[ask_for_input()] = player2
print_board(board)
# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.
