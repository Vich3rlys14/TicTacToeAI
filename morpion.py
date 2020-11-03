#-*-coding:utf-8-*-
# !/usr/bin/python 3.5.2

import math 
import time
import pygame
from pygame.locals import *
from ticTacToeIA import *
from Board import *

white = 0xffffff
red = 0xff0000
blue = 0x0000ff
black = 0x000000

xsign , osign = 'x' , 'o'

def drawCircle(pos, bg, case_size):
	x,y = pos
	centerx , centery = int(case_size/2)+x, int(case_size/2)+y
	pygame.draw.circle(bg, red, (centerx,centery), int((case_size-10)/2) )
	pygame.draw.circle(bg, white, (centerx,centery), int((case_size-20)/2) )

def drawCross(pos, bg, case_size):
	x , y = pos
	line1StartX , line2StartX = x+5 , x+case_size -5
	line1StartY , line2StartY = y+5 , y+5
	line1StopX , line2StopX = x+case_size-5 , x+5
	line1StopY , line2StopY = y+case_size-5 , y+case_size-5
	
	pygame.draw.line(bg, blue, (line1StartX ,line1StartY ), (line1StopX ,line1StopY ) , 6)
	pygame.draw.line(bg, blue, (line2StartX ,line2StartY ), (line2StopX ,line2StopY ) , 6)

def drawBoard( board , bg, case_size )	:
	for y , row in enumerate(board.board):
		for x, case in enumerate(row) :
			pos  = (x*case_size, y*case_size)
			if case == xsign :
				drawCross ( pos, bg, case_size)
			elif case == osign:
				drawCircle( pos, bg, case_size)

def drawCases(bg , case_size , nb_case):
	for  i in range(nb_case-1):
		pygame.draw.line(bg, black, (0, ((i+1)*case_size) ), (case_size*nb_case, ((i+1)*case_size) ) , 1)
		pygame.draw.line(bg, black, (((i+1)*case_size), 0 ), (((i+1)*case_size), case_size*nb_case ) , 1)


def captureClick(coord, case_size):
	return (coord[0]//case_size , coord[1]//case_size)


def main():
	pygame.init()

	#global variables
	case_size = 50
	done = False

	# tic tac toe board initialization
	board = Board()
	# graphic initialization
	screen = pygame.display.set_mode((case_size*board.boardlen,case_size*board.boardlen))
	background = pygame.Surface(screen.get_size())
	background.fill(white)
	screen.blit(background , (0,0))

	turn  = 0
	#game initialization
	
	while not done:
		#cur_sign = osign if (turn%2) == 0 else xsign	
		for event in pygame.event.get():
			if event.type == QUIT:
				done = True

			elif event.type == MOUSEBUTTONDOWN:
				coord = captureClick(pygame.mouse.get_pos() , case_size)
				if (board.fill( coord , osign )):
															
				
					if board.checkWin() == osign:
						print (" player win !!" )
						done = True
					elif isDraw(board.board):
						print("draw!!!")
						done = True
					else :
					
						AImove = search(board , xsign , osign )
						board.fill(AImove , xsign)
						if board.checkWin() == xsign:
							print (" the computer win !!")
							done = True

		drawBoard(board, background, case_size)
		drawCases(background, case_size , board.boardlen)
		screen.blit(background,(0,0))
		
		pygame.display.update() 

if __name__ == '__main__':
	main()
