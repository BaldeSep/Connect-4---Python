from tkinter import *

class Connect_4():
    def __init__(self, master = None):
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.root = master

        self.player_1_image = PhotoImage(file = 'Images\\player_1.png')
        self.player_2_image = PhotoImage(file = 'Images\\player_2.png')
        self.empty = PhotoImage(file = 'Images\\empty.png')
        
        self.labels = [[Label(self.root, image = self.empty ,height = 50, width = 50) for x in range(7)] for y in range(6)]
        self.init_labels()

        self.turn = 1
        
    def init_labels(self):
        for c in range(7):
            for r in range(6):
                self.labels[r][c].grid(row = r, column = c)
                self.labels[r][c].bind('<Button-1>', lambda event, col = c: self.place_peace(event, col))

    def place_peace(self, event, col):
        next_avail_row = -1
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                next_avail_row = row
                break
        if next_avail_row == -1:
            print('Invalid Position')
            return
        else:
            self.board[next_avail_row][col] = self.turn
            self.update_image(next_avail_row, col)

        self.checkWinning(next_avail_row, col)
        
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

        for i in range(6):
            for j in range(7):
                print(self.board[i][j], end = ' ')
            print()
        else:
            print()

    def checkWinning(self, row, col):
        # check south
        if row + 3 < len(self.board):
            if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                print('Player', self.board[row][col], 'won!!!')

        # check east
        if col + 3 < len(self.board[row]):
            if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                print('Player', self.board[row][col], 'won!!!')

        # check west
        if col - 3 >= 0:
            if self.board[row][col] == self.board[row][col-1] == self.board[row][col-2] == self.board[row][col-3]:
                print('Player', self.board[row][col], 'won!!!')

        # check north-east
        if row - 3 >= 0 and col + 3 < len(self.board[row]):
            if self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]:
                print('Player', self.board[row][col], 'won!!!')

        # check north-west
        if row - 3 >= 0 and col - 3 >= 0:
            if self.board[row][col] == self.board[row-1][col-1] == self.board[row-2][col-2] == self.board[row-3][col-3]:
                print('Player', self.board[row][col], 'won!!!')

        # check south-east
        if row + 3 < len(self.board) and col + 3 < len(self.board[row]):
            if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                print('Player', self.board[row][col], 'won!!!')

        # check south-west
        if row + 3 < len(self.board) and col - 3 >= 0:
            if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3]:
                print('Player', self.board[row][col], 'won!!!')
        
    def update_image(self, row, col):
        if self.turn == 1:
            self.labels[row][col].config(image = self.player_1_image)
        elif self.turn == 2:
            self.labels[row][col].config(image = self.player_2_image)
    
root = Tk()

Connect_4(root)

root.mainloop()
