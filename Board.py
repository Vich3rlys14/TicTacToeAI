class Board():
	def __init__(self , boardlen  = 3 ):
		self.boardlen = boardlen
		self.board = [ [None for x in range(boardlen)] for x in range(boardlen)]
	
	def checkWin(self):
		diag1,diag2 = True, True
		for i in range(self.boardlen):
			vert , horz, = True , True
			for j in range(self.boardlen-1):
				if horz:
					if self.get(i,j) != self.get(i,j+1):
						horz = False
				if vert:
					if self.get(j,i) != self.get(j+1,i):
						vert = False
				if diag1:
					if self.get(j+1, j+1) != self.get(j,j):
						diag1 = False
				if diag2:
					if self.get((self.boardlen-1)-(j+1), (j+1)) != self.get((self.boardlen-1)-j,j):
						diag2 = False
			if vert:
				return self.get(0,i)
			if horz:
				return self.get(i,0)
			if diag1:
				return self.get(0,0)
			if diag2:
				return self.get(self.boardlen-1,0)
		return False

	def get(self,x,y):
		return self.board[y][x]

	def checkDraw(self):
		pass

	def fill(self, coord, content):
		if self.board[coord[1]][coord[0]] != None:
			return False
		self.board[coord[1]][coord[0]] = content
		return True
	
	def __repr__(self):
		text =""
		for row in self.board:
			for elt in row :
				
				text = text+ elt if elt !=None else text+" "

		return text
				


