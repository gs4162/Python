import logging
import time
logging.basicConfig(level=logging.INFO)

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
boardmap = [['7','8','9'],['4','5','6'],['1','2','3']]
game_on = True

def main(board):
    #intro
    message_printer('Welcome to Tik-Tak-Toe')
    message_printer()  # Space out the message
    show_board(board)
    message_printer()  # Space out the message
    message_printer('Here is what the board looks like, Each number = a position')
    show_board(boardmap)

    # Start play
    message_printer()  # Space out the message
    while game_on:
        # Player 1's turn
        valid_move = False
        while not valid_move:  # Keep asking until a valid move is made
            valid, player1_input = validate_input(input('Player 1, please select a position where you want your X: [1-9]: '))
            while not valid:  # Validate the input
                print('ERROR: Player 1, please select a position where you want your X: [1-9]: ')
                show_board(boardmap)
                valid, player1_input = validate_input(input('Player 1, please select a position where you want your X: [1-9]: '))
            
            board, valid_move = update_board(board, player1_input, 'X')  # Update the board and check if the move is valid
            show_board(board)
        check_winner(board)

        if not game_on:
            break

        # Player 2's turn
        valid_move = False
        while not valid_move:  # Keep asking until a valid move is made
            valid, player2_input = validate_input(input('Player 2, please select a position where you want your O: [1-9]: '))
            while not valid:  # Validate the input
                print('ERROR: Player 2, please select a position where you want your O: [1-9]: ')
                show_board(boardmap)
                valid, player2_input = validate_input(input('Player 2, please select a position where you want your O: [1-9]: '))

            board, valid_move = update_board(board, player2_input, 'O')  # Update the board and check if the move is valid
            show_board(board)
        check_winner(board)

        if not game_on:
            break

    print('Done')





def message_printer(message=''):
    print(message)

def show_board(board):
    print()
    for row in board:
        print(row)
    print()

def validate_input(user_input):
    if not user_input: #Check for blank input
        return False, None
    if not user_input.isdigit():
        return False, None
    try:
        user_input = int(user_input) #Ensure the input can be converted to a int
    except ValueError:
        return False, None
    if user_input in range(1, 10):  #Ensure the input is in range.
        return True, user_input
    else:
        return False, None

def update_board(board,player_input,symb):
    position_map = {
        1: (2, 0), 2: (2, 1), 3: (2, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (0, 0), 8: (0, 1), 9: (0, 2)
    }
    row,col = position_map[player_input]

    #print(f'{board} {player_input} {symb} {row} {col}')
    if board[row][col] == ' ':
        board[row][col]=symb
        return(board, True)
    else:
        print('Invalid selection. Position already taken.')
        print()
        print('Here is the key to position mapping:')
        show_board(boardmap)
        return board, False  

def check_winner(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            print(f"Player {row[0]} wins!")
            game_over()
            return

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            print(f"Player {board[0][col]} wins!")
            game_over()
            return

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        print(f"Player {board[0][0]} wins!")
        game_over()
        return
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        print(f"Player {board[0][2]} wins!")
        game_over()
        return

    # Check if the board is full (i.e., a tie)
    if all(cell != ' ' for row in board for cell in row):
        print("It's a tie!")
        game_over()

def game_over():
    global game_on
    game_on = False

if __name__ == "__main__":
    main(board)