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


def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-|-|-")
    pass
def create_board():
    """
    creates and returns a new board (list of strings)

    """
    board = [1,2,3,4,5,6,7,8,9]
    #for spot in range(1, 10):
       # board.append(spot)
    
def get_user_choice():
    """
    asks the user for their choice of spot on the board
    """
    pass
def is_tie_game(board):











if __name__ == "__main__":
    main()