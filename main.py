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
        self.front_view = ''

    def reveal(self):
        pass

    def flag(self):
        pass


class MineField:
    def __init__(self):
        pass
    
    def print_field(self):
        pass


