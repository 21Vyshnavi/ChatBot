import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or        all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def minimax(board, is_maximizing):
    if check_winner(board, 'O'): return 1
    if check_winner(board, 'X'): return -1
    if is_full(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    temp = board[i][j]
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = temp
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    temp = board[i][j]
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = temp
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                temp = board[i][j]
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = temp
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print_board(board)

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        i, j = divmod(move, 3)
        if board[i][j] in ['X', 'O']:
            print("Invalid move. Try again.")
            continue
        board[i][j] = 'X'
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("Draw!")
            break

        i, j = best_move(board)
        board[i][j] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("Draw!")
            break

main()
