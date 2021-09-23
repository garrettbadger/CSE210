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
    
    board = create_board()
    display_board(board)
    tile = get_user_choice()
    new_board = modify_board(board, tile)
    display_board(new_board)
    is_game_over(new_board)


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
    
def get_user_choice():
    """
    Asks the user for their choice of spot on the board.
    """
    turn = 0
    tile = []
    while turn %2 == 0:
        tile.append("X")
        tile.append(input("X's turn! Where would you like to play? (1-9):"))
        turn += 1
        return tile
    else:
        tile.append("O")
        tile.append(input("O's turn! Where would you like to play? (1-9):"))
        turn +=1
        return tile
def modify_board(board, tile):
    place = int(tile[1]) - 1
    if tile[0] == "X":
        board.pop(place)
        board.insert(place, "X")
    else:
        board.pop(place)
        board.insert(place, "O")
    return board

def is_game_over(board):
    if board[0, 1, 2] == "X" or "O":
        print("Game Over!")
    


def is_tie_game(board):
    pass











if __name__ == "__main__":
    main()