"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x=0
    o=0
    for row in board:
        for column in row:
            if column == 'X':
                x+=1
            elif column == 'O':
                o+=1
    
    if x<=o:
        return X
    return O
    raise NotImplementedError


def actions(board):
    answer = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                answer.add((i,j))
    return answer
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x,y = action
    if board[x][y]!= None:
        return board
    move = player(board)
    board [x][y]=move
    return board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #across
    if board[0][0]==board[0][1] and board[0][1]==board[0][2]:
        if board[0][0]==X:
            return X
        else:
            return O
        
    if board[1][0]==board[1][1] and board[1][1]==board[1][2]:
        if board[1][0]==X:
            return X
        else:
            return O
        
    if board[2][0]==board[2][1] and board[2][1]==board[2][2]:
        if board[2][0]==X:
            return X
        else:
            return O
        
    #down
    if board[0][0]==board[1][0] and board[1][0]==board[2][0]:
        if board[0][0]==X:
            return X
        else:
            return O
    if board[0][1]==board[1][1] and board[1][1]==board[2][1]:
        if board[0][1]==X:
            return X
        else:
            return O
    if board[0][2]==board[1][2] and board[1][2]==board[2][2]:
        if board[0][0]==X:
            return X
        else:
            return O
    
    #diagonal
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]==X:
            return X
        else:
            return O
    if board[0][2]==board[1][1] and board[1][1]==board[0][2]:
        if board[0][2]==X:
            return X
        else:
            return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==None:
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
    
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
