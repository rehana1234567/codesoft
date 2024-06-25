import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return 10
        elif row.count("O") == 3:
            return -10
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == "O":
            return -10
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        return -10
    
    # No winner
    return 0

def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return True
    return False

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    elif not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = " "
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while is_moves_left(board):
        if player == "X":
            print("Player X's turn:")
            move = input("Enter your move (row[1-3] column[1-3]): ")
            row, col = map(int, move.split())
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("Invalid move! Try again.")
                continue
            board[row][col] = "X"
        else:
            print("AI's turn (Player O):")
            row, col = find_best_move(board)
            board[row][col] = "O"
        
        print_board(board)
        
        score = evaluate(board)
        if score == 10:
            print("Player X wins!")
            break
        elif score == -10:
            print("Player O wins!")
            break
        
        player = "X" if player == "O" else "O"
    
    if score == 0:
        print("It's a draw!")

play_game()
