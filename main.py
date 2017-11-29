from tkinter import *
from tkinter import messagebox


class Connect_4():
	def __init__(self, master = None):
		self.root = master
		self.board = [[0 for x in range(7)] for y in range(6)]
	
		self.root.title('Connect 4')
		
		self.init_drop_window()
		
		self.turn = 1
		
		self.init_status_bar()
		
		self.player_1_image = PhotoImage(file = 'Images/player_1.png')
		self.player_2_image = PhotoImage(file = 'Images/player_2.png')
		self.empty = PhotoImage(file = 'Images/empty.png')
        
		self.labels = [[Label(self.root, image = self.empty ,height = 48, width = 48) for x in range(7)] for y in range(6)]
		self.init_labels()
		
		
	def init_status_bar(self):
		self.status = Label(self.root, text = 'Player Turn: ' + str(self.turn) ,  bd = 1, relief = SUNKEN, anchor = W)
		self.status.grid(row = 6, columnspan = 7)
		
	def init_drop_window(self):
		self.menu = Menu(self.root)
		self.root.config(menu = self.menu)
		self.submenu = Menu(self.menu)
		self.menu.add_cascade(label = 'Options', menu = self.submenu)
		self.submenu.add_command(label = 'Reset', command = self.reset)
		self.submenu.add_command(label = 'Exit', command = self.root.destroy)
	
	def reset(self):
		for r in range(0, len(self.board)):
			for c in range(0, len(self.board[r])):
				self.board[r][c] = 0
				self.labels[r][c].config(image = self.empty)
		
		self.turn = 1
		
		self.status.config(text = 'Player Turn: ' + str(self.turn))
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
			messagebox.showinfo(title = 'Error', message = 'Invalid Move')
			return
		else:
			self.board[next_avail_row][col] = self.turn
			self.update_image(next_avail_row, col)

		if self.checkWinning(next_avail_row, col) == True:
			messagebox.showinfo('Winner!!!', 'Player ' + str(self.turn) + ' Wins!!!')
			self.reset()
			return
        
		if self.turn == 1:
			self.turn = 2
		elif self.turn == 2:
			self.turn = 1
			
		self.status.config(text = 'Player Turn: ' + str(self.turn))
		
		
		for i in range(6):
			for j in range(7):
				print(self.board[i][j], end = ' ')
			print()
		else:
			print()
	
	
	def checkWinning(self, row, col):
		board_h = len(self.board)
		board_w = len(self.board[row])
		
		# check East then West
		counter = 1
		next_left_col = col - 1
		next_right_col = col + 1
		while next_left_col >= 0 and self.board[row][next_left_col] == self.turn:
			counter += 1
			next_left_col -= 1
			if counter == 4:
				return True
		
		while next_right_col < board_w and self.board[row][next_right_col] == self.turn:
			counter +=1 
			next_right_col += 1
			if counter == 4:
				return True
				
		
		# check South
		counter = 1
		next_row = row + 1
		while next_row < board_h and self.board[next_row][col] == self.turn:
			next_row += 1
			counter += 1
			if counter == 4:
				return True
		
		
		# check North East then South West
		counter = 1
		next_north_row = row - 1
		next_south_row = row + 1
		next_right_col = col + 1
		next_left_col = col - 1
		while next_north_row >= 0 and next_right_col < board_w and self.board[next_north_row][next_right_col] == self.turn:
			next_north_row -= 1
			next_right_col += 1
			counter += 1
			if counter == 4:
				return True
		
		while next_south_row < board_h and next_left_col >= 0 and self.board[next_south_row][next_left_col] == self.turn:
			next_south_row += 1
			next_left_col -= 1
			counter += 1
			if counter == 4:
				return True
		
		
		# check South East then North West
		counter = 1
		next_south_row = row + 1
		next_right_col = col + 1
		next_north_row = row - 1
		next_left_col = col - 1
		while next_south_row < board_h and next_right_col < board_w and self.board[next_south_row][next_right_col] == self.turn:
			next_south_row += 1
			next_right_col += 1
			counter += 1
			if counter == 4:
				return True
		
		while next_north_row >= 0 and next_left_col >= 0 and self.board[next_north_row][next_left_col] == self.turn:
			next_north_row -= 1
			next_left_col -= 1
			counter +=1 
			if counter == 4:
				return True
				
	def update_image(self, row, col):
		if self.turn == 1:
			self.labels[row][col].config(image = self.player_1_image)
		elif self.turn == 2:
			self.labels[row][col].config(image = self.player_2_image)
    
root = Tk()

Connect_4(root)


root.mainloop()
