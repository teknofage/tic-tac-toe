# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

BOARD_SIZE = 10

def draw_board(board):
    """This function prints out the board that it was passed."""

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second."""
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def who_goes_first():
    """Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def play_again():
    """This function returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much."""
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)   # diagonal
        ) 

def get_board_copy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    dupeBoard = []

    for i in range(len(board)):
        dupeBoard.append(board[i])

    return dupeBoard

def in_space_free(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def get_player_move(board):
    """Let the player type in their move."""
    next_turn = ' ' 
    while next_turn not in '1 2 3 4 5 6 7 8 9'.split() or not in_space_free(board, int(next_turn)):
        print('What is your next move? (1-9)')
        next_turn = input()
    return int(next_turn)

def choose_random_move_from_list(board, movesList):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    possible_moves = []
    for i in movesList:
        if in_space_free(board, i):
            possible_moves.append(i)

    if possible_moves: 
        return random.choice(possible_moves)
    return None

def get_computer_move(board, ai_team): 
    """Given a board and the computer's letter, determine where to move and return that move."""
    if ai_team is 'X':
        player_team = 'O'
    else:
        player_team = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, BOARD_SIZE):
        copy = get_board_copy(board)
        if in_space_free(copy, i):
            make_move(copy, ai_team, i)
            if is_winner(copy, ai_team):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, BOARD_SIZE):
        copy = get_board_copy(board)
        if in_space_free(copy, i):
            make_move(copy, player_team, i)
            if is_winner(copy, player_team):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None: 
        return move

    # Try to take the center, if it is free.
    if in_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def game_is_playing(turn):
	draw_board(the_board)
	move = get_computer_move(the_board, ai_team)
	make_move(the_board, ai_team, move)

    if is_board_full(the_board):
        draw_board(the_board)
		print('The game is a tie!')
		return False
    
    elif turn is 'player':
		# Player’s turn.
		if is_winner(the_board, player_team):
			draw_board(the_board)
			print('Hooray! You have won the game!')
			return False
		elif:
			turn = 'computer'
			return True

	else:
		# Computer’s turn.
		if is_winner(the_board, ai_team):
			draw_board(the_board)
			print('The computer has beaten you! You lose.')
			return = False
		elif: 
			turn = 'player'
			return True

def is_board_full(board):
    """Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1, BOARD_SIZE):
        if in_space_free(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. Use TODO s and the comment above each section as a guide 
# for refactoring.

while True:
    # Reset the board
    the_board = [' '] * BOARD_SIZE 
    player_team, ai_team = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    
    game_is_playing() == True 

    if not play_again():
        break