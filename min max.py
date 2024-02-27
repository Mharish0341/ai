def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def evaluate(board):
    # Check rows, columns, and diagonals for a win or loss
    for row in board:
        if all(cell == 'X' for cell in row):
            return 1
        elif all(cell == 'O' for cell in row):
            return -1

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 1
        elif all(board[row][col] == 'O' for row in range(3)):
            return -1

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -1

    return 0  # No winner, game is a draw

def is_terminal(board):
    return any(cell == '' for row in board for cell in row) or evaluate(board) != 0

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

def minimax(board, depth, maximizing_player):
    if is_terminal(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ''  # Undo the move
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ''  # Undo the move
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        move_val = minimax(board, 0, False)
        board[i][j] = ''  # Undo the move

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

# Example usage:
board = [['', '', ''], ['', '', ''], ['', '', '']]
print_board(board)

while not is_terminal(board):
    player_move = tuple(map(int, input("Enter your move (row and column): ").split()))
    if board[player_move[0]][player_move[1]] == '':
        board[player_move[0]][player_move[1]] = 'O'
        print_board(board)
    else:
        print("Invalid move, try again.")

    if not is_terminal(board):
        computer_move = find_best_move(board)
        print("Computer's move:", computer_move)
        board[computer_move[0]][computer_move[1]] = 'X'
        print_board(board)

winner = evaluate(board)
if winner == 1:
    print("You lose!")
elif winner == -1:
    print("You win!")
else:
    print("It's a draw!")
