""" This Program implements the tic tac toe using regular minimax. """
__author__= "Abhilash Peddinti"

# importing the libraries
from random import choice
from math import inf as infinity

# assigning values for Human and AI
HUMAN= -1
AI = +1

# values in the game board
game_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def terminal_function(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current game board
    :return: +10 if the computer wins; -10 if the human wins; 0 for draw
    """
    if wins(state, HUMAN): # checking the conditions to see who won
        utility= -10
    elif wins(state, AI):
        utility = +10
    else:
        utility = 0

    return utility

def empty_squares(state):
    """
    Each empty square is added into the squares list
    :param state: the state of the current board
    :return: a list of empty squares on board
    """
    squares = []

    for x, row in enumerate(state):          # looping through the game board
        for y, square in enumerate(row):
            if square == 0: squares.append([x, y])         # adding the empty squares
    return squares

def valid_move(x, y): #--
    """
    A move is valid if the chosen square is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_squares(game_board):
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, AI)


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_states = [                                      # assigning the win states
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_states:
        return True
    else:
        return False

def design(state, AI_choice, HUMAN_choice):
    """
    Print the board on console
    :param state: current state of the board
    """
    print('----------------')
    for row in state:
        print('\n----------------')
        for square in row:
            if square == +1:
                print('[', AI_choice, ']', end='')
            elif square == -1:
                print('[', HUMAN_choice, ']', end='')
            else:
                print('[', ' ', ']', end='')
    print('\n----------------')


def set_move(a, b, player):
    """
    Set the move on board, if the coordinates are valid
    :param a: X coordinate
    :param b: Y coordinate
    :param player: the current player
    """
    if valid_move(a,b):
        game_board[a][b] = player
        return True
    else:
        return False


def regular_minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """

    global count
    count = count + 1
    if player == HUMAN:
        best = [-1, -1, infinity]
    else:
        best = [-1, -1, -infinity]

    if depth == 0 or game_over(state):
        score = terminal_function(state)
        return [-1, -1, score]

    for square in empty_squares(state):
        x, y = square[0], square[1]
        state[x][y] = player
        score = regular_minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == HUMAN:
            if score[2] < best[2]:
                best = score  # max value
        else:
            if score[2] > best[2]:
                best = score  # min value

    return best




def ai_turn(AI_choice, HUMAN_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_squares(game_board))
    if depth == 0 or game_over(game_board):
        return


    design(game_board, AI_choice, HUMAN_choice)
    print('Computer turn [{}]'.format(AI_choice))

    if depth != 9:
        global count
        count=0
        move = regular_minimax(game_board, depth, AI)
        a, b = move[0], move[1]
    else:
        a = choice([0, 1, 2])
        b = choice([0, 1, 2])

    set_move(a, b, AI)
    print(a,b,"Position")
    print("The AI generated" +" "+ str(count) +" " + "nodes")



def human_turn(AI_choice, HUMAN_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_squares(game_board))
    if depth == 0 or game_over(game_board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    print('Human turn [{}]'.format(HUMAN_choice))
    design(game_board, AI_choice, HUMAN_choice)

    while (move < 1 or move > 9):
        try:
            move = int(input('Enter the position to place using 1 to 9: '))
            coord = moves[move]
            try_move = set_move(coord[0], coord[1], HUMAN)

            if try_move == False:
                print('Enter the correct position')
                move = -1
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    print("Welcome to Tic Tac Toe")
    print("Human will play against AI")
    print("First move is maken by human")
    HUMAN_choice = 'X'

    first = ''  # if human is the first

    # Human chooses X or O to play


    # Setting computer's choice
    AI_choice = 'O'
    # Human may starts first


    # Main loop of this game
    while len(empty_squares(game_board)) > 0 and not game_over(game_board):
        human_turn(AI_choice, HUMAN_choice)
        ai_turn(AI_choice, HUMAN_choice)

    # Game over message
    if wins(game_board, AI):
        print('Computer turn [{}]'.format(AI_choice))
        design(game_board, AI_choice, HUMAN_choice)
        print('YOU LOST THE GAME')

    elif  wins(game_board, HUMAN):
        print('Human turn [{}]'.format(HUMAN_choice))
        design(game_board, AI_choice, HUMAN_choice)
        print('YOU WON THE GAME')
    else:
        design(game_board, AI_choice, HUMAN_choice)
        print('THE GAME IS DRAW!')

    exit()


if __name__ == '__main__':
    main()