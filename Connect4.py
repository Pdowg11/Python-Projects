import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROWS = 6
COLUMNS = 7

def create_board():
  board = np.zeros((ROWS, COLUMNS))
  return board

def place_piece(board, row, col, piece):
  board[row][col] = piece

def valid_check(board, col):
  return board[ROWS-1][col] == 0

def check_next_row(board, col):
  for r in range(ROWS):
    if board[r][col] == 0:
      return r

def print_board(board):
  print(np.flip(board, 0))
  
def win_check(board, piece):
  for c in range(COLUMNS-3):
    for r in range(ROWS):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True
  
  for c in range(COLUMNS):
    for r in range(ROWS-3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True

  for c in range(COLUMNS-3):
    for r in range(ROWS-3):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True

  for c in range(COLUMNS-3):
    for r in range(3, ROWS):
      if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        return True

def draw_board(board):
  for c in range(COLUMNS):
    for r in range(ROWS):
      pygame.draw.rect(screen, BLUE, (c*WINDOWSIZE, r*WINDOWSIZE+WINDOWSIZE, WINDOWSIZE, WINDOWSIZE))
      pygame.draw.circle(screen, BLACK, (int(c*WINDOWSIZE+WINDOWSIZE/2), int(r*WINDOWSIZE+WINDOWSIZE+WINDOWSIZE/2)), RADIUS)

  for c in range(COLUMNS):
    for r in range(ROWS):
      if board[r][c] == 1:
        pygame.draw.circle(screen, RED, (int(c*WINDOWSIZE+WINDOWSIZE/2), height-int(r*WINDOWSIZE+WINDOWSIZE/2)), RADIUS)
      elif board[r][c] == 2:
        pygame.draw.circle(screen, YELLOW, (int(c*WINDOWSIZE+WINDOWSIZE/2), height-int(r*WINDOWSIZE+WINDOWSIZE/2)), RADIUS)
  pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

WINDOWSIZE = 100

width = COLUMNS * WINDOWSIZE
height = (ROWS+1) * WINDOWSIZE

size = (width, height)

RADIUS = int(WINDOWSIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font = pygame.font.SysFont('sans', 75)

while not game_over:
  for  event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.MOUSEMOTION:
      pygame.draw.rect(screen, BLACK, (0, 0, width, WINDOWSIZE))
      xpos = event.pos[0]
      if turn == 0:
        pygame.draw.circle(screen, RED, (xpos, int(WINDOWSIZE/2)), RADIUS)
      else:
        pygame.draw.circle(screen, YELLOW, (xpos, int(WINDOWSIZE/2)), RADIUS)
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
      pygame.draw.rect(screen, BLACK, (0,0, width, WINDOWSIZE))
      if turn == 0:
        xpos = event.pos[0]
        col = int(math.floor(xpos/WINDOWSIZE))

        if valid_check(board, col):
          row = check_next_row(board, col)
          place_piece(board, row, col, 1)

          if win_check(board, 1):
            label = font.render('Player 1 wins!', 1, RED)
            screen.blit(label, (40, 10))
            game_over = True


      else:
        xpos = event.pos[0]
        col = int(math.floor(xpos/WINDOWSIZE))

        if valid_check(board, col):
          row = check_next_row(board, col)
          place_piece(board, row, col, 2)

          if win_check(board, 2):
            label = font.render('Player 2 wins!', 1, YELLOW)
            screen.blit(label, (40, 10))
            game_over = True

      print_board(board)
      draw_board(board)

      turn = turn + 1
      turn = turn % 2

      if game_over:
        sys.exit()