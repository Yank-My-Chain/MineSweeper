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
        self.cells = []

        # Create 2D array of 'Cells'
        for i in range(WIDTH):
            for j in range(HEIGHT):
                self.cells.append(Cell)
    
    def print_field(self):
        for cell_row in self.cells:
            for cell in cell_row:
                cell.splash()
            print('')


if __name__ == '__main__':
    game = MineField()

    game.print_field()

    wait = input('')


