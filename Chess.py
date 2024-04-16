EMPTY = " "
black = ["r", "n", "b", "q", "k", "p"]
white = ["R", "N", "B", "Q", "K", "P"]

def print_board(board):
    # Prints the chess board.

    for row in range(8):
        print(" +---+---+---+---+---+---+---+---+")
        print(f"{8 - row}| ", end="")
        for col in range(8):
            print(f"{board[row][col]} | ", end="")
        print()

    print(" +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h")

def initialize_board():
    # Initializes the chess board with pieces.

    return [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p"] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        ["P"] * 8,
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]

def is_valid_move(board, start, end, turn):
    # Checks if the move is valid.

    start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord("a")
    end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord("a")

    piece = board[start_row][start_col]
    target_piece = board[end_row][end_col]

    # Check if the move is within the board

    if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
        return False

    # Check if the piece belongs to the current player's turn

    if (turn == "white" and piece.islower()) or (turn == "black" and piece.isupper()):
        return False

    # Check if the target square contains a piece of the same color

    if (piece in black and target_piece in black) or (piece in white and target_piece in white):
        return False

    # Specific move validations for each piece type

    if piece.lower() == "p":
        if start_col == end_col:
            if turn == "white" and start_row - end_row == 1 and target_piece == EMPTY:
                return True
            elif turn == "black" and start_row - end_row == -1 and target_piece == EMPTY:
                return True
            elif (
                    (turn == "white" and start_row == 6 and start_row - end_row == 2 and all(
                        board[i][end_col] == EMPTY for i in
                        range(end_row + 1, start_row + 1)) and target_piece == EMPTY)
                    or (turn == "black" and start_row == 1 and start_row - end_row == -2 and all(
                board[i][end_col] == EMPTY for i in range(start_row + 1, end_row + 1)) and target_piece == EMPTY)
            ):
                return True
        elif abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1:
            if (
                    (turn == "white" and start_row - end_row == 1 and target_piece.isupper())
                    or (turn == "black" and start_row - end_row == -1 and target_piece.islower())
            ):
                return True
    elif piece.lower() == "n":
        return (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or (
                    abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2)  # Knight move
    elif piece.lower() == "b":
        return abs(start_row - end_row) == abs(start_col - end_col)  # Bishop move
    elif piece.lower() == "r":
        return start_row == end_row or start_col == end_col  # Rook move
    elif piece.lower() == "q":
        return start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(
            start_col - end_col)  # Queen move
    elif piece.lower() == "k":
        return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1  # King move

    return False

def apply_move(board, move):
    # Applies the given move to the chess board.

    start, end = move
    start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord("a")
    end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord("a")

    piece = board[start_row][start_col]
    board[start_row][start_col] = EMPTY
    board[end_row][end_col] = piece

def main():
    # Main function to run the chess game.

    board = initialize_board()
    turn = "white"

    while True:
        print("White Pieces are Capital Letters \nBlack Pieces are Small Letters")
        print_board(board)
        print(f"{turn.capitalize()}'s turn")

        move = input("Enter your move (e.g., 'e2 e4'): ").split()

        if len(move) != 2:
            print("Invalid move format. Please enter two valid positions.")
            continue

        if not is_valid_move(board, move[0], move[1], turn):
            print("Invalid move. Please try again.")
            continue

        apply_move(board, move)

        turn = "black" if turn == "white" else "white"

if __name__ == "__main__":
    main()