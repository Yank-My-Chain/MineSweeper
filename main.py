import string
from random import randint

# Symbols for squares
UNTOUCHED = '-'
BLANK = 'O'
FLAGGED = '/'
BOMB = 'X'

# Corners
CORNERS = (
    {'x': -1, 'y': 1},
    {'x': 1, 'y': 1},
    {'x': 1, 'y': -1},
    {'x': -1, 'y': -1}
)

FACES = (
    {'x': 0, 'y': 1},
    {'x': 1, 'y': 0},
    {'x': 0, 'y': -1},
    {'x': -1, 'y': 0},
)

# Field size
WIDTH = 10
HEIGHT = 10

# Total bombs
TOTAL_BOMBS = 20

# GAME_OVER
GAME_OVER = False

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
        self.revealed = True

    def is_revealed(self):
        return self.revealed

    def flag(self):
        pass

    def set_as_bomb(self):
        self.contains_bomb = True
    
    def set_touching_bombs(self, bombs):
        self.touching_bombs = bombs

    def splash(self):
        print(self.front_view, end='')

    def set_as_flagged(self):
        self.flagged = True
        self.front_view = FLAGGED

    def show_cell(self):
        if self.flagged:
            return
        elif self.contains_bomb:
            self.front_view = BOMB
        elif self.touching_bombs == 0:
            self.front_view = BLANK
        elif self.touching_bombs > 0:
            self.front_view = str(self.touching_bombs)

        self.reveal()


class MineField:
    def __init__(self):
        # Generate the 2D list of cells
        self.cells = [[0 for x in range(WIDTH)] for x in range(HEIGHT)]
        self.cells:list(list(Cell))
        for i in range(HEIGHT):
            for j in range(WIDTH):
                self.cells[i][j] = Cell()

        self.columns = list(string.ascii_lowercase[:WIDTH])
        self.rows = [str(number) for number in range(0, HEIGHT)]

    def get_cell(self, row:int , column:int ) -> Cell:
        if row < 0 or column < 0:
            cell = None
            return cell
        try:
            cell = self.cells[row][column]
        except IndexError:
            cell = None
        return cell

    def _does_bomb_exist(self, row, column):
        if row < 0 or column < 0:
            return False
        try:
            return self.get_cell(row, column).contains_bomb
        except IndexError:
            return False
        except AttributeError:
            return False
    
    def set_bombs(self, total_bombs):
        for x in range(total_bombs):
            self.get_cell(randint(0,WIDTH-1),randint(0,HEIGHT-1)).set_as_bomb()

    def _find_cells_touching_bombs(self, row, column):
        bombs_touching = 0
        for row_index in [row+row_offset for row_offset in range(-1,2,1)]:
            for column_index in [column+column_offset for column_offset in range(-1,2,1)]:
                if row_index == row and column_index == column:
                    continue
                if self._does_bomb_exist(row_index,column_index):
                    bombs_touching += 1
        self.get_cell(row,column).set_touching_bombs(bombs_touching)

    def set_all_touching_bombs(self):
        for _i in range(0,HEIGHT):
            for _j in range(0,WIDTH):
                self._find_cells_touching_bombs(_i,_j)

    def _reveal_all_cells(self):
        # Should not be used. Simply a debug call
        for _i in range(0,HEIGHT,1):
            for _j in range(0,WIDTH,1):
                self.cells[_i][_j].show_cell()

    def reveal_request(self, row:int, column:int):
        cell = self.get_cell(row, column)
        if not cell:
            # Probably out of range at this point
            return
        
        if cell.flagged:
            # Can't reveal a flagged cell
            return
        
        cell.show_cell()
        if cell.contains_bomb:
            GAME_OVER = True
            return
        if cell.touching_bombs > 0:
            return
        for next_location in FACES:
            next_cell = self.get_cell(row + next_location['x'], column + next_location['y'])
            if next_cell is None:
                continue
            elif next_cell.is_revealed():
                continue
            else:
                self.reveal_request(row + next_location['x'], column + next_location['y'])

class CommandLineGame:
    def __init__(self, mine_game: MineField) -> None:
        self.game = mine_game
    
    def print_field(self):
        print(' ', end='')
        for header in self.game.columns:
            print(header, end='')
        print('')
    
        for iter, cell_row in enumerate(self.game.cells):
            print(self.game.rows[iter], end='')
            for cell in cell_row:
                cell.splash()
            print('')

    def _print_hidden_field(self):
        print(' ', end='')
        for header in self.game.columns:
            print(header, end='')
        print('')
    
        for iter, cell_row in enumerate(self.game.cells):
            print(self.game.rows[iter], end='')
            for cell in cell_row:
                if cell.contains_bomb:
                    print('X', end='')
                else:
                    print(f'{cell.touching_bombs}', end='')
            print('')

    def ask_for_cell(self):
        input_row = input('What row: ')
        input_column = input('What column: ')
        cell_row = int(input_row)
        cell_column = int(input_column)
        self.game.reveal_request(cell_row, cell_column)
        self.print_field()


if __name__ == '__main__':
    game = MineField()
    cmd_game = CommandLineGame(game)
    game.set_bombs(TOTAL_BOMBS)
    game.set_all_touching_bombs()
    cmd_game._print_hidden_field()
    cmd_game.print_field()
    cmd_game.ask_for_cell()
'''
 abcdefghij
0000012X100
100001X2100
20000111000
30000011100
4000001X210
50000012X10
60111013320
701X211XX21
8012X11222X
90011100011


 abcdefghij
0OOOO1--1OO
1OOOO1-21OO
2OOOO111OOO
3OOOOO111OO
4OOOOO1-21O
5OOOOO1--1O
6O111O1--2O
7O1-211--21
8O12------X
9OO1------1
'''