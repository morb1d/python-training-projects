"""
Tic Tac Toe Game 
Written as part of Udemy course: Complete Python Bootcamp
"""
def tic_tac_toe():
    board = [" "] * 9
    game_in_progress = True
    player1 = "X"
    player2 = "O"
    player_playing = player1

    def print_board(game_board):
        for i, value in enumerate(game_board):
            if (i < 2 and i != 1):
                print(' %s ' %(value), end='')
            elif (i > 2 and i < 5 and i != 4):
                print(' %s ' %(value), end='')
            elif (i > 5 and i < 8 and i != 7):
                print(' %s ' %(value), end='')
            elif (i == 2 or i == 5 or i == 8):
                print(' %s ' %(value))
                if (i != 8):
                    print("---|---|---")
            elif (i == 1 or i == 4 or i == 7):
                print('| %s |' %(value), end='')
            else:
                pass

    def ask_for_input(player):
        if(player=="X"):
            player_input = int(input("Player1: Your choice? "))    
        else: 
            player_input = int(input("Player2: Your choice? "))    
        return player_input

    def validate_if_place_is_available(input, game_board):
        if (game_board[input] != " "):    
            print("Field is used already, try another one.")
            return False
        else:
            return True

    def player_switch(player):
        if(player==player1):
            return player2
        else:
            return player1

    def check_game_state(game_board,player):
        game_tied = next((x for x in game_board if x==" "), True)
        if ((game_board[0] == game_board[1] == game_board[2] != " ") or
            (game_board[3] == game_board[4] == game_board[5] != " ") or
            (game_board[6] == game_board[7] == game_board[8] != " ") or
            (game_board[0] == game_board[3] == game_board[6] != " ") or
            (game_board[1] == game_board[4] == game_board[7] != " ") or 
            (game_board[2] == game_board[5] == game_board[8] != " ") or 
            (game_board[0] == game_board[4] == game_board[8] != " ") or 
            (game_board[2] == game_board[4] == game_board[6] != " ")):
            print(player," has won.")
            return False
        elif (game_tied):
            print("Game tied.")
            return False
        else:
            return True
        
    while(game_in_progress):
        
        player_input = ask_for_input(player_playing)
        if(validate_if_place_is_available(player_input, board)):
            board[player_input] = player_playing
            print_board(board)
            game_in_progress = check_game_state(board,player_playing)
            player_playing = player_switch(player_playing)

    play_again = input("Do you want to play again? (Yes/No): ")        
    if(play_again == "Yes"):
        return True
    else:
        return False

game_on = True
while (game_on):  
    game_on = tic_tac_toe()
