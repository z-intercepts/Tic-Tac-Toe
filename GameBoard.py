class GameBoard:
    __board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    #               0 | 1 | 2
    #               ---------
    #               3 | 4 | 5
    #               ---------
    #               6 | 7 | 8

    __player_one = " "
    __player_two = " "

    # Constructs a game board object
    def __init__(self, player_one, player_two):
        self.__player_one = player_one
        self.__player_two = player_two

    def check_player(self, player):
        if player == 1:
            return self.__player_one
        elif player == 2:
            return self.__player_two
        else:
            print("Error incorrect player")
            return

    def check_tie(self):
        if (self.__board[0] != "0" and self.__board[1] != "1" and self.__board[2] != "2" and
            self.__board[3] != "3" and self.__board[4] != "4" and self.__board[5] != "5" and
                self.__board[6] != "6" and self.__board[7] != "7" and self.__board[8] != "8"):
            print("Game Tied!")
            self.print_board()
            self.__board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
            return True

    # Returns true if current player has win conditions met
    def check_win(self, player):
        letter = self.check_player(player)

        if (self.__board[0] == letter and self.__board[1] == letter and self.__board[2] == letter
                or self.__board[3] == letter and self.__board[4] == letter and self.__board[5] == letter
                or self.__board[6] == letter and self.__board[7] == letter and self.__board[8] == letter
                or self.__board[0] == letter and self.__board[3] == letter and self.__board[6] == letter
                or self.__board[1] == letter and self.__board[4] == letter and self.__board[7] == letter
                or self.__board[2] == letter and self.__board[5] == letter and self.__board[8] == letter
                or self.__board[0] == letter and self.__board[4] == letter and self.__board[8] == letter
                or self.__board[2] == letter and self.__board[4] == letter and self.__board[6] == letter):
            print("Player #%d wins" % player)
            self.print_board()
            self.__board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
            return player

    # edits board[]'s position using player's character
    # returns true if spot if empty else returns false
    def edit_board(self, player, position):
        letter = self.check_player(player)

        if self.__board[position] != "X" and self.__board[position] != "O":
            self.__board[position] = letter
            return True
        else:
            print("Position already filled")
            return False

    def empty_spots(self):
        i = 0
        empty = []
        for var in self.__board:
            if self.__board[var] != "X" and self.__board[var] != "O":
                empty[i] = var
                i = i + 1
        return empty

    # returns the board
    def get_board(self):
        return self.__board

    def print_board(self):
        print(" %s |  %s  |  %s " % (self.__board[0], self.__board[1], self.__board[2]))
        print("--------------")
        print(" %s |  %s  |  %s " % (self.__board[3], self.__board[4], self.__board[5]))
        print("--------------")
        print(" %s |  %s  |  %s \n" % (self.__board[6], self.__board[7], self.__board[8]))
