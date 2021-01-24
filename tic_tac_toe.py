def print_matrix(matrix):
    print("---------")
    for row in matrix:
        print("|", " ".join(row), "|")
    print("---------")

def verify_status(matrix):
    for row in matrix:
        if row == list("XXX") or row == list("OOO"):
            return True, "wins"
    for i in range(3):
        col = [row[i] for row in matrix]
        if col == list("XXX") or col == list("OOO"):
            return True, "wins"
    diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
    if diagonal == list("XXX") or diagonal == list("OOO"):
        return True, "wins"
    diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
    if diagonal == list("XXX") or diagonal == list("OOO"):
        return True, "wins"
    if not len([x for row in matrix for x in row if x not in "XO"]):
        return True, "Draw"
    return False, ""

def get_coordinates():
    while True:
        coordinates = input("Enter the coordinates:").split()
        nums = list("0123456789")
        if coordinates[0] not in nums or len(coordinates) > 1 and coordinates[0] not in nums:
            print("You should enter numbers!")
            continue
        x, y = int(coordinates[0]), int(coordinates[1])
        if not 0 < x < 4 or not 0 < y < 4:
            print("Coordinates should be from 1 to 3!")
            continue
        return x - 1, y - 1

def next_move(matrix):
    while True:
        x, y = get_coordinates()
        if matrix[x][y] in "XO":
            print("This cell is occupied! Choose another one!")
            continue
        return x, y

matrix = [[" ", " ", " "] for _ in range(3)]
print_matrix(matrix)
x_turn, ended = False, False
while not ended:
    x_turn = not x_turn
    x, y = next_move(matrix)
    matrix[x][y] = 'X' if x_turn else 'O'
    print_matrix(matrix)
    ended, message = verify_status(matrix)    
print(message if message == "Draw" else "X " + message if x_turn else "O " + message)
