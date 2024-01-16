def print_board(board):
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print()

def check_winner(board, player):
    # Check horizontally
    for row in board:
        for col in range(4):
            if row[col:col + 4] == [player] * 4:
                return True

    # Check vertically
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == player:
                return True

    # Check diagonally (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == player:
                return True

    # Check diagonally (top-left to bottom-right)
    for row in range(3):
        for col in range(3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == player:
                return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_connect4():
    board = [[" " for _ in range(7)] for _ in range(6)]
    current_player = "X"

    while True:
        print_board(board)
        col = int(input(f"Player {current_player}, choose a column (1-7): ")) - 1

        for row in range(5, -1, -1):
            if board[row][col] == " ":
                board[row][col] = current_player
                break
        else:
            print("Column is full. Please choose another column.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_connect4()
