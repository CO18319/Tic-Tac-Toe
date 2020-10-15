# Symbols for representing AI and human in tic-tac-toe board
ai = 'X'
human = 'O'

# Size of tic-tac-toe board
size = 3

# scores representing the ending possibilities of a game
scores = {
    'X': 10,
    'O': -10,
    'tie': 0
}

# colors representing ai and human player
colour = {human: "deep sky blue", ai: "lawn green"}


# static evaluation function which returns the number
# representing the goodness of board position for a player
def static(result):
    if result == ai:
        return scores[ai]
    elif result == human:
        return scores[human]
    else:
        return scores['tie']


# function to check if three board positions have the same symbol
def equals(pos1, pos2, pos3):
    return pos1 == pos2 and pos2 == pos3 and pos1 != '_'


# function to check the board position for a win or a tie
def check_winner(board):
    winner = ""

    # check all rows for a win
    for i in range(size):
        if equals(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]

    # check all columns for a win
    for i in range(size):
        if equals(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]

    # check two diagonals for a win
    if equals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]

    if equals(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]

    # check if there are empty positions on the board
    open_spots = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == '_':
                open_spots = open_spots + 1

    # there is a tie if all cells on the board are filled
    # and none of the player wins else return the winner
    if winner == "" and open_spots == 0:
        return 'tie'
    else:
        return winner


# function to generate all possible moves for a board position
def move_gen(board):
    empty_cells = []

    # store a cell if it is empty
    for i in range(size):
        for j in range(size):
            if board[i][j] == '_':
                empty_cells.append([i, j])
    return empty_cells


class solve:

    def __init__(self):
        # tuple of lists representing tic-tac-toe cells
        self.board = (
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        )

    def minimax(self, board, player):
        # check if there is a win or a tie representing the terminal board position
        result = check_winner(board)

        # return value of static evaluation function board position it is a terminal position
        if result != "":
            return static(result)

        # calculate value of board position if player is maximizing i.e ai or minimizing i.e human
        if player == ai:
            # set minimum score for maximizing player
            score = - 9999
            # generate all possible moves
            empty_position = move_gen(board)
            for i, j in empty_position:
                board[i][j] = ai
                current_score = self.minimax(board, human)
                board[i][j] = "_"
                score = max(score, current_score)
            return score
        else:
            # set maximum score for minimizing player
            score = 9999
            # generate all possible moves
            empty_position = move_gen(board)
            for i, j in empty_position:
                board[i][j] = human
                current_score = self.minimax(board, ai)
                board[i][j] = "_"
                score = min(score, current_score)
            return score

    # function to find best move for ai player
    def best_move(self):
        best_score = -9999
        row = -1
        col = -1

        # place ai at all empty board cells
        # and check for best cell
        for i in range(size):
            for j in range(size):
                if self.board[i][j] == '_':
                    self.board[i][j] = ai
                    score = self.minimax(self.board, human)
                    self.board[i][j] = '_'
                    if score > best_score:
                        best_score = score
                        row = i
                        col = j
        self.board[row][col] = ai
        return [row, col]
