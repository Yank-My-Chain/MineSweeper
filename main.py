import string

# Symbols for squares
UNTOUCHED = '-'
BLANK = 'O'
FLAGGED = '/'
BOMB = 'X'

# Field size
WIDTH = 10
HEIGHT = 10

class Cell:
    def __init__(self):
        self.contains_bomb = False
        self.touching_bombs = 0
        self.flagged = False
        self.revealed = False
        self.front_view = UNTOUCHED

    def __repr__(self):
        pass

    def reveal(self):
        pass

    def flag(self):
        pass

    def splash(self):
        print(self.front_view, end='')


class MineField:
    def __init__(self):
        # Generate the 2D list of cells
        self.cells = [[0 for x in range(WIDTH)] for x in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(WIDTH):
                self.cells[i][j] = Cell()

        self.columns = list(string.ascii_lowercase[:WIDTH])
        self.rows = [str(number) for number in range(0, HEIGHT)]
    
    def print_field(self):
        print(' ', end='')
        for header in self.columns:
            print(header, end='')
        print('')
    
        for iter, cell_row in enumerate(self.cells):
            print(self.rows[iter], end='')
            for cell in cell_row:
                cell.splash()
            print('')


if __name__ == '__main__':
    game = MineField()

    game.print_field()
