from tkinter import *
from tkinter import messagebox


class Connect_4():
	def __init__(self, master = None):
		
		self.board = [[0 for x in range(7)] for y in range(6)]
		self.root = master
	
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

		self.checkWinning(next_avail_row, col)
        
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
		board_height = len(self.board)
		board_width = len(self.board[row])
        
		
		# check South
		if (row+1) < board_height:
			if self.board[row+1][col] == self.turn:
				print()	
		
		# check East
		if (col+1) < board_width:
			if self.board[row][col+1] == self.turn:
				print()
				
		# check West
		if (col-1) >= 0:
			if self.board[row][col-1] == self.turn:
				print()
				
		# check North East
		if (col+1) < board_width and (row-1) >= 0:
			if self.board[row-1][col+1] == self.turn:
				print()
				
		# check North West
		if (row-1) >= 0 and (col-1) >= 0:
			if self.board[row-1][col-1] == self.turn:
				print()
				
		# check South East
		if (row+1) < board_height and (col+1) < board_width:
			if self.board[row+1][col+1] == self.turn:
				print()
				
		# check South West
		if (row+1) < board_height and (col-1) >= 0:
			if self.board[row+1][col-1] == self.turn:
				print()
			
			
			 
				
        
        
	def update_image(self, row, col):
		if self.turn == 1:
			self.labels[row][col].config(image = self.player_1_image)
		elif self.turn == 2:
			self.labels[row][col].config(image = self.player_2_image)
    
root = Tk()

Connect_4(root)

root.mainloop()
