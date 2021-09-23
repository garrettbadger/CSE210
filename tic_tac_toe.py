"""
Candidate Variables:
-players
-current_player
- board
-
-
-
-
Candidate Functions:
-display_board
-is_game_over
-check_win
-is_draw
-write_in_board
-make_move
-display_current_user
"""
def main():
    gameover = False
    turn = 0
    board = create_board()
    tie = False
    display_board(board)
    for i in range(9):
        
        tile = get_user_choice(board, turn)
        new_board = modify_board(board, tile)
        display_board(new_board)
        gameover = is_game_over(new_board)
        tie = is_tie_game(new_board)
        if tie == True:
            print("The game is a draw!")
            break
        else:
            pass
        if gameover == True:
            if turn %2 == 0:
                print("X Won!")
            else:
                print("O Won!")
            break
        
        turn += 1
    


def display_board(board):
    """
    Displays the board to the user.
    """
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    
    
def create_board():
    """
    Creates and returns a new board (list of strings).

    """
    board = []
    
    for spot in range(1, 10):
        board.append(spot)
    
    return board
    
def get_user_choice(board, turn):
    """
    Asks the user for their choice of spot on the board.
    """
    board = board
    #turn = 0
    tile = []
    while turn %2 == 0:
        tile.append("X")
        tile.append(input("X's turn! Where would you like to play? (1-9):"))
        #turn += 1
        #modify_board(board, tile)
        return tile
    else:
        tile.append("O")
        tile.append(input("O's turn! Where would you like to play? (1-9):"))
        #turn +=1
        #modify_board(board, tile)
        return tile
    
def modify_board(board, tile):
    """
    Adds a players X or O to the board.
    """
    place = int(tile[1]) - 1
    if tile[0] == "X":
        board.pop(place)
        board.insert(place, "X")
    else:
        board.pop(place)
        board.insert(place, "O")
    #is_game_over(board)
    return board

def is_game_over(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

#def is_game_over(board):
#    """
#    Checks to see if game is over.
#    """
#    
#    if board[0:3] == "X":
#        print("Game Over!")
#        return True
#        
#    elif board[0:3] == "O":
#        print("Game Over!")
#        return True
#
#    elif board[3:6] == "X":
#        print("Game Over")
#        return True
#
#    elif board[3:6] == "O":
#        print("Game Over")
#        return True
#
#    elif board[6:9] == "X":
#        print("Game Over")
#        return True
#
#    elif board[6:9] =="O":
#        print("Game Over")
#        return True
#
#    elif board[0] == "X":
#        if board[3] =="X":
#            if board[6] =="X":
#
#                print("Game Over")
#                return True
#
#    elif board[0] == "O":
#        if board[3] =="O":
#            if board[6] =="O":
#
#                print("Game Over")
#                return True
#
#    elif board[1] == "X":
#        if board[4] =="X":
#            if board[7] =="X":
#
#                print("Game Over")
#                return True
#
#    elif board[1] == "O":
#        if board[4] =="O":
#            if board[7] =="O":
#
#                print("Game Over")
#                return True
#
#    elif board[2] == "X":
#        if board[5] =="X":
#            if board[8] =="X":
#
#                print("Game Over")
#                return True
#
#    elif board[2] == "O":
#        if board[5] =="O":
#            if board[8] =="O":
#
#                print("Game Over")
#                return True
#
#    elif board[0] == "X":
#        if board[4] =="X":
#            if board[8] =="X":
#
#                print("Game Over")
#                return True
#
#    elif board[0] == "O":
#        if board[4] =="O":
#            if board[8] =="O":
#
#                print("Game Over")
#                return True
#
#    elif board[2] == "X":
#        if board[4] =="X":
#            if board[6] =="X":
#
#                print("Game Over")
#                return True
#    
#    elif board[2] == "O":
#        if board[4] =="O":
#            if board[6] =="O":
#
#                print("Game Over")
#                return True
#
#    else: 
#        return False
#        
        #get_user_choice(board)

    


def is_tie_game(board):
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            return False
        
    return True











if __name__ == "__main__":
    main()