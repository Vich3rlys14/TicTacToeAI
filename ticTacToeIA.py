import collections 
from Board import *
import random

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections

lists = collectionsAbc.MutableSequence
def copy_list(arr):
	copy = []
	for i,elt in enumerate(arr):
		if isinstance( elt , lists):
			copy.append(copy_list(elt))
		else :
			copy.append(elt)
	return copy

def isDraw(board):
	for row in board:
		for elt in row:
			if elt == None:
				return False
	return True

		
def think_naively(board , sign):
	current_board = copy_list(board.board)
	coord =  (random.randrange(3) , random.randrange(3))
	if (isDraw(current_board)):
		return False

	while board.get(coord[0] , coord[1]) != None:
		coord =  (random.randrange(3) , random.randrange(3))
	return coord

def get_empty_spots(board , length):
	empty_spots =  []
	for y in range(length):
		for x in range(length):
			if  board[y][x] == None:
				empty_spots.append((x,y))
	return empty_spots

def test_move (board , p , sign):
	copy_board =  Board()
	copy_board.board = copy_list(board.board)
	copy_board.fill( p , sign	)
	return copy_board


explored = {}

def search(board , sign, esign ):
	"""function used to choose an optimal move"""
	opt_value  = 0
	opt_moves = []
	empt_spots = get_empty_spots(board.board, board.boardlen)
	
	if len(empt_spots) == 1:
		return empt_spots[0]
	
	n =0
	for p in empt_spots :
		
		copy_board =  test_move(board , p  , sign)
		move_value = eval_board(copy_board, sign , esign )
			
		if n < 1 :
			opt_value = move_value
			n+=1

		if opt_value == move_value :
			opt_moves.append(p)

		elif opt_value < move_value :
			opt_moves = []
			opt_moves.append(p)
			opt_value = move_value		

	return random.choice(opt_moves)
 

def eval_board(board , sign , esign , n=0 ):
	"""evaluate board value"""
	boardname = board.__repr__()
	if boardname in explored.keys():
		return explored[boardname][sign]

	win = board.checkWin()
	
	if win :
		if win == sign :
			explored[boardname] = {}
			explored[boardname][sign] = 10
			explored[boardname][esign] = -10
			return 10
		elif win == esign:
			explored[boardname] = {}
			explored[boardname][sign] = -10
			explored[boardname][esign] = 10
			return -10

	if isDraw(board.board):
		explored[boardname] = {}
		explored[boardname][sign] = 0
		explored[boardname][esign] = 0
		return 0

	else:
		S = []
		for p in get_empty_spots(board.board , board.boardlen):
			cp_board = test_move(board , p ,esign)
			beval = (eval_board(cp_board , esign  , sign , n+1 ))
			S.append(-beval)

		boardval =  sum(S)/ 10 #closer possibility of win or loss are more valued
		explored[boardname] = {}
		explored[boardname][sign] = boardval
		explored[boardname][esign] = -boardval
		return boardval