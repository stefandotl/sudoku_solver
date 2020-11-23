

board = [
         [0,8,0,7,0,1,0,3,0],
         [4,0,9,0,0,0,0,0,0],
         [0,5,0,0,6,0,4,1,8],
         [7,0,0,0,0,9,0,0,0],
         [8,0,0,6,1,0,5,0,0],
         [0,3,5,0,0,0,0,2,9],
         [0,6,0,4,0,7,0,9,0],
         [1,0,0,0,0,8,0,0,4],
         [0,2,0,0,5,0,0,7,0]
]

def board_printing(board):

    for j, row in enumerate(board):
        for i, digit in enumerate(row):
            print(digit, " ", end='')
            if i % 3 == 2 and i != 0:
                print("| ", end='')

        print("")
        if j % 3 == 2 and j != 7:
            print("--------------------------------")


def check_empty(board):
    """returns the position of an empty field"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None


def valid(board, number, position):
    """checks if the digit is on a valid position"""

    x = position[0]
    y = position[1]

    # checks row
    for i in range(9):
        if board[x][i] == number:
            return False

    # checks column
    for i in range(9):
        if board[i][y] == number:
            return False

    # check square
    square_x = x // 3
    square_y = y // 3

    for i in range(square_x * 3, square_x * 3 + 3):
        for j in range(square_y * 3, square_y * 3 + 3):
            if board[i][j] == number:
                return False

    return True


def find_solution(board):
    """recursively checks if digit is on a valid position"""

    global found_solution
    empty_position = check_empty(board)

    if empty_position is None:
        found_solution = True

    if found_solution:
        return True
    else:
        row, column = empty_position

    for i in range(1,10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if find_solution(board):
                return True

            board[row][column] = 0

    return False


if __name__ == "__main__":
    found_solution = False
    find_solution(board)
    board_printing(board)





