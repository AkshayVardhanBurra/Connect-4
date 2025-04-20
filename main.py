from board import Board

ROWS = 6
COLUMNS = 7
board = Board(ROWS, COLUMNS)


running = True

def get_valid_input(phrase):
    valid_input = input(f"{phrase}: Enter a position (1 - 7)")

    if valid_input == "quit":
        return valid_input
                        
    valid_input = int(valid_input)
   
    while valid_input < 1 or valid_input > COLUMNS or board.check_column_full(valid_input - 1):
        valid_input = int(input("Enter a valid range (1-7) that isn't full: "))
    
    return valid_input

def set_player_choices():
    char_1 = input("Enter a character other than O for player 1: ")
    while(char_1.upper() == "O"):
        char_1 = input("Enter a character other than O for player 1: ")
    
    Board.PLAYER_1 = char_1

    char_2 = input("Enter a character other than O for player 2: ")
    while(char_2.upper() == "O" or char_2 == char_1):
        char_2 = input("Enter a character other than O for player 2: ")
    
    Board.PLAYER_2 = char_2


def print_board():
    print("\n------------------------------------------")
    board.print_board()
    print("------------------------------------------\n")


set_player_choices()
print_board()
while running:

    

    
    player_1 = get_valid_input("Player 1")
    print("player_1: " + str(player_1 - 1))
    
    board.add_piece(player_1 - 1, Board.PLAYER_1)
    print_board()
    if board.check_win(Board.PLAYER_1):
        print("PLAYER 1 WON!")
        break

    elif player_1 == "quit":
        break;
    elif board.board_full():
        print("Board is full!")
        break

    player_2 = get_valid_input("Player 2")
    board.add_piece(player_2 - 1, Board.PLAYER_2)
    print_board()
    if board.check_win(Board.PLAYER_2):
        print("PLAYER 2 WON!")
        break
    elif player_2 == "quit":
        break
    elif board.board_full():
        print("Board is full!")
        break








