winner = False
board_completed = False
player = "X"

empty_matrix = [[" " for _ in range(3)] for _ in range(3)]

columns = {
    "A": 0,
    "B": 1,
    "C": 2,
}

def display_board(m):
    print("   A B C")
    for i in range(0, 3):
        print(f"{i + 1}  ", end="")
        for j in range(0, 3):
            print(m[i][j], end="|")
        print("\n")


def enter_move(position_asked):
    col = columns[position_asked[0]]
    row = int(position_asked[1]) - 1
    return (row, col)


def new_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


while not winner and not board_completed:
    print("Possible Values: A1, A2, A3, B1, B2, B3, C1, C2, C3")

    while True:
        position_asked = input(f"Choose a position {player}: ")
        if position_asked in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            break
        else:
            print("Invalid position. Please choose a value from Possible position.")

    row, col = enter_move(position_asked)

    if empty_matrix[row][col] == " ":
        empty_matrix[row][col] = player
        display_board(empty_matrix)
        if check_winner(empty_matrix, player):
            print(f"Player {player} wins!")
            winner = True
        elif all(cell != " " for row in empty_matrix for cell in row):
            print("It's a tie!")
            board_completed = True
        else:
            player = "O" if player == "X" else "X" 
    else:
        print("Position is not available")




