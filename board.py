class Board:

    PLAYER_1 = "1"

    PLAYER_2 = "2"

    def __init__(self, rows, cols):

        self.board = self.empty_board(rows, cols)


    def empty_board(self, rows, cols):
        empty_board = []
        for i in range(rows):
            line = []
            for a in range(cols):
                line.append("O")
            empty_board.append(line)

        return empty_board

            
    

    def add_piece(self, col, p_char):
        
        for i in range(len(self.board)):
            if self.board[i][col] == Board.PLAYER_1 or self.board[i][col] == Board.PLAYER_2:
           
                if i - 1 < 0:
                    return
                else:
                    self.board[i - 1][col] = p_char
                    return
        self.board[len(self.board) - 1][col] = p_char
        
    
    def check_column_full(self, col):

        for i in range(len(self.board)):
            if self.board[i][col] == "O":
                return False
        
        return True
    
    def board_full(self):

        for i in range(7):
            if not self.check_column_full(i):
                return False
        
        return True


    def check_win(self, p_char):
        for i in range(len(self.board)):
            for a in range(len(self.board[i])):
                if self.board[i][a] == p_char:
                    if self.__test_dirs__(i, a):
                        return True
        return False

            


    def __test_dirs__(self, i, a):
        return (self.__find_win_path__(i, a, 1,0) or self.__find_win_path__(i, a, 0, 1) or self.__find_win_path__(i, a, -1, 0) or self.__find_win_path__(i, a, 0, -1)
                or self.__find_win_path__(i, a, 1, 1) or self.__find_win_path__(i, a, -1, 1) or self.__find_win_path__(i, a, -1, -1) or self.__find_win_path__(i,a, 1, -1) )

    def __find_win_path__ (self, row, col, r_add, c_add):

        if not self.__in_bounds__(row, col):
            return False
        
        curr_row = row
        curr_col = col

        char = self.board[curr_row][curr_col]
        counter = 0
        while self.__in_bounds__(curr_row, curr_col) and self.board[curr_row][curr_col] == char and counter < 4:
            curr_row += r_add
            curr_col += c_add
            counter += 1

        
        return counter == 4
    

    def __in_bounds__(self, row, col):
        return row >= 0 and row < len(self.board) and col >= 0 and col < len(self.board[row])

    def print_board(self):
        for line in self.board:
            print(line)


        
        




        

