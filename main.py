from tabulate import tabulate
import colorama
from colorama import Fore

# Chess pieces are global to modify at run

board = {}

# Row 1
board['a1'] = 'R'
board['b1'] = 'N'
board['c1'] = 'B'
board['d1'] = 'Q'
board['e1'] = 'K'
board['f1'] = 'B'
board['g1'] = 'N'
board['h1'] = 'R'

# Row 2
board['a2'] = 'P'
board['b2'] = 'P'
board['c2'] = 'P'
board['d2'] = 'P'
board['e2'] = 'P'
board['f2'] = 'P'
board['g2'] = 'P'
board['h2'] = 'P'

# Row 3
board['a3'] = ' '
board['b3'] = ' '
board['c3'] = ' '
board['d3'] = ' '
board['e3'] = ' '
board['f3'] = ' '
board['g3'] = ' '
board['h3'] = ' '

# Row 4
board['a4'] = ' '
board['b4'] = ' '
board['c4'] = ' '
board['d4'] = ' '
board['e4'] = ' '
board['f4'] = ' '
board['g4'] = ' '
board['h4'] = ' '

# Row 5
board['a5'] = ' '
board['b5'] = ' '
board['c5'] = ' '
board['d5'] = ' '
board['e5'] = ' '
board['f5'] = ' '
board['g5'] = ' '
board['h5'] = ' '

# Row 6
board['a6'] = ' '
board['b6'] = ' '
board['c6'] = ' '
board['d6'] = ' '
board['e6'] = ' '
board['f6'] = ' '
board['g6'] = ' '
board['h6'] = ' '


# Row 7
board['a7'] = 'P'
board['b7'] = 'P'
board['c7'] = 'P'
board['d7'] = 'P'
board['e7'] = 'P'
board['f7'] = 'P'
board['g7'] = 'P'
board['h7'] = 'P'


# Row 8
board['a8'] = 'R'
board['b8'] = 'N'
board['c8'] = 'B'
board['d8'] = 'Q'
board['e8'] = 'K'
board['f8'] = 'B'
board['g8'] = 'N'
board['h8'] = 'R'

def drawBoard(move1, move2):

	if move1 != ' ':  # When move is empty print a clear start up position board
		clean_move1, piece1 = determinePiece(move1, 'W')
		clean_move2, piece2 = determinePiece(move2, 'B')

		board[clean_move1] = piece1
		board[clean_move2] = piece2

	table=[[board['a8'],board['b8'],board['c8'],board['d8'],board['e8'],board['f8'],board['g8'],board['h8']],
	     [board['a7'], board['b7'], board['c7'], board['d7'], board['e7'], board['f7'], board['g7'], board['h7']],
	     [board['a6'], board['b6'], board['c6'], board['d6'], board['e6'], board['f6'], board['g6'], board['h6']],
		 [board['a5'], board['b5'], board['c5'], board['d5'], board['e5'], board['f5'], board['g5'], board['h5']],
		 [board['a4'], board['b4'], board['c4'], board['d4'], board['e4'], board['f4'], board['g4'], board['h4']],
	     [board['a3'], board['b3'], board['c3'], board['d3'], board['e3'], board['f3'], board['g3'], board['h3']],
	     [board['a2'], board['b2'], board['c2'], board['d2'], board['e2'], board['f2'], board['g2'], board['h2']],
	     [board['a1'], board['b1'], board['c1'], board['d1'], board['e1'], board['f1'], board['g1'], board['h1']]]


	print(tabulate(table, tablefmt='fancy_grid'))

def determinePiece(move, color):
	keyPieces = ['R', 'N', 'B', 'Q', 'K']

	if move[0] not in keyPieces:
		piece = 'P'
		clean_move = move
		pawnMovement(clean_move, color)

	else:
		piece = move[0]
		clean_move = move[1:]

	return clean_move, piece


def pawnMovement(s, color):
	# two steps only if row 2 for white and 7 for Black everything else one to move forward
	s.split()  # get 1st the column then the number

	if color == 'W':
		# if row is 4 and row 2 is occupied decrease 2 movements
		x = s[0]
		y = int(s[1]) - 1 # while moves forward

	elif color == 'B':
		x = s[0]
		y = int(s[1]) + 1  # black  moves backwards

	clearCell = str(x) + str(y)  # while clears at the back minus
	board[clearCell] = ' '


# Main Function
drawBoard(' ',' ') #clear the board
drawBoard('d3', 'd6') # Draw pawn move
input("Press Enter to continue...")
drawBoard('Nc3', 'Nc6') # Draw knight move
input("Press Enter to continue...")
drawBoard('a3', 'h6')
