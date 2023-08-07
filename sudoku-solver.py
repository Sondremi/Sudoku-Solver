
def find_next_empty(puzzle):
    # Finner den første tomme ruten
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    # Hvis det ikke et noen tomme ruter
    return None, None        

def is_valid(puzzle, guess, row, col):
    # Sjekker om gjettet tall er i raden
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Sjekker om gjettet tall er i kolonnen
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # Sjekker om gjettet tall er i boksen
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):

    row, col = find_next_empty(puzzle)

    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        # Hvis det ikke er et valid gjett
        puzzle[row][col] = -1 
    
    # Hvis det ikke finnes en løsning
    return False


if __name__ == '__main__':
    # Endre brettet etter opplysningene du har
    brett = [
        [4, -1, -1,   6, -1, 8,   -1, -1, -1],
        [9, 1, -1,   -1, 3, 2,   8, -1, 6],
        [-1, 8, 3,   -1, 1, -1,   -1, -1, 2],

        [-1, -1, 2,   8, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   1, -1, -1,   3, -1, 5],
        [5, -1, 8,   -1, 7, 4,   -1, -1, -1],

        [-1, -1, -1,   -1, -1, -1,   -1, -1, 8],
        [-1, -1, -1,   -1, -1, -1,   2, -1, -1],
        [-1, 7, -1,   -1, 9, 6,   4, -1, 3]
    ]
    print(f"\nDet finnes en løsning til spillet: {solve_sudoku(brett)}\n")

    teller_rad = 0
    teller_kolonne = 0

    for rad in range(len(brett)):
        for kolonne in range(len(brett[rad])):
            print(brett[rad][kolonne], end=' ')
            teller_kolonne += 1
            if teller_kolonne == 3:
                print(' ', end='')
                teller_kolonne = 0
        print("")
        teller_rad += 1
        if teller_rad == 3:
            print("")
            teller_rad = 0



# Kopier og lim inn dette brettet for å nullstille
nytt_brett = [
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],

    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],

    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1]
]