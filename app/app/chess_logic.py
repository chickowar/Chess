class MoveMaker:
    board = list('tMvWlVmTOoOoOoOo + + + ++ + + +  + + + ++ + + + pPpPpPpPRnBqKbNr')
    turn = 'white'
    proper_pos = {'a8': 0, 0: 'a8',
                  'b8': 1, 1: 'b8',
                  'c8': 2, 2: 'c8',
                  'd8': 3, 3: 'd8',
                  'e8': 4, 4: 'e8',
                  'f8': 5, 5: 'f8',
                  'g8': 6, 6: 'g8',
                  'h8': 7, 7: 'h8',
                  'a7': 8, 8: 'a7',
                  'b7': 9, 9: 'b7',
                  'c7': 10, 10: 'c7',
                  'd7': 11, 11: 'd7',
                  'e7': 12, 12: 'e7',
                  'f7': 13, 13: 'f7',
                  'g7': 14, 14: 'g7',
                  'h7': 15, 15: 'h7',
                  'a6': 16, 16: 'a6',
                  'b6': 17, 17: 'b6',
                  'c6': 18, 18: 'c6',
                  'd6': 19, 19: 'd6',
                  'e6': 20, 20: 'e6',
                  'f6': 21, 21: 'f6',
                  'g6': 22, 22: 'g6',
                  'h6': 23, 23: 'h6',
                  'a5': 24, 24: 'a5',
                  'b5': 25, 25: 'b5',
                  'c5': 26, 26: 'c5',
                  'd5': 27, 27: 'd5',
                  'e5': 28, 28: 'e5',
                  'f5': 29, 29: 'f5',
                  'g5': 30, 30: 'g5',
                  'h5': 31, 31: 'h5',
                  'a4': 32, 32: 'a4',
                  'b4': 33, 33: 'b4',
                  'c4': 34, 34: 'c4',
                  'd4': 35, 35: 'd4',
                  'e4': 36, 36: 'e4',
                  'f4': 37, 37: 'f4',
                  'g4': 38, 38: 'g4',
                  'h4': 39, 39: 'h4',
                  'a3': 40, 40: 'a3',
                  'b3': 41, 41: 'b3',
                  'c3': 42, 42: 'c3',
                  'd3': 43, 43: 'd3',
                  'e3': 44, 44: 'e3',
                  'f3': 45, 45: 'f3',
                  'g3': 46, 46: 'g3',
                  'h3': 47, 47: 'h3',
                  'a2': 48, 48: 'a2',
                  'b2': 49, 49: 'b2',
                  'c2': 50, 50: 'c2',
                  'd2': 51, 51: 'd2',
                  'e2': 52, 52: 'e2',
                  'f2': 53, 53: 'f2',
                  'g2': 54, 54: 'g2',
                  'h2': 55, 55: 'h2',
                  'a1': 56, 56: 'a1',
                  'b1': 57, 57: 'b1',
                  'c1': 58, 58: 'c1',
                  'd1': 59, 59: 'd1',
                  'e1': 60, 60: 'e1',
                  'f1': 61, 61: 'f1',
                  'g1': 62, 62: 'g1',
                  'h1': 63, 63: 'h1'}
    pieces = {
        "BlackKing": 'l',
        "BlackQueen": 'w',
        "BlackKnight": 'm',
        "BlackBishop": 'v',
        "BlackRook": 't',
        "BlackPawn": 'o',

        "WhiteKing": 'k',
        "WhiteQueen": 'q',
        "WhiteKnight": 'n',
        "WhiteBishop": 'b',
        "WhiteRook": 'r',
        "WhitePawn": 'p'
    }
    black_pieces = {'l', 'L', 'w', 'W', 'm', 'M', 'v', 'V', 't', 'T', 'o', 'O'}
    white_pieces = {'k', 'K', 'q', 'Q', 'n', 'N', 'b', 'B', 'r', 'R', 'p', 'P'}

    def __init__(self, board: str | list | None = None) -> None:
        if board is not None:
            self.board = list(board)
        pass

    def proper_board(self, for_console=False):
        """Returns a board in 8 lines, not in 1 line.
        If you set for_console to True it will divide rows by '/n',
        otherwise it will divide them by '<br />' for HTML."""
        if for_console:
            delim = '\n'
        else:
            delim = '<br />'
        ret = ''
        for i in range(8):
            i8 = i*8
            ret += ('|' +
                    self.board[i8] +
                    self.board[i8+1] +
                    self.board[i8+2] +
                    self.board[i8+3] +
                    self.board[i8+4] +
                    self.board[i8+5] +
                    self.board[i8+6] +
                    self.board[i8+7] +
                    delim)
        return ret

    def change_turn(self) -> None:
        """
        Changes the turn from black to white
        or from white to black
        """
        self.turn = 'black' if self.turn == 'white' else 'white'
        pass

    def colorize_tile(self, pos: int) -> None:
        """
        Changes the color of the tile to
        the appropriate color
        """
        row = pos >> 3  # division by 8
        col = pos & 7  # pos % 8
        if (row+col) & 1 == 0:  # if (row+col) % 2 == 0 - WHITE
            if self.board[pos] == '+':
                self.board[pos] = ' '
            else:
                self.board[pos] = self.board[pos].lower()
        else:  # else BLACK
            if self.board[pos] == ' ':
                self.board[pos] = '+'
            else:
                self.board[pos] = self.board[pos].upper()
        pass

    def check_piece_color_(self, pos: int) -> str:
        """
        Checks the color of the piece on the tile

        returns 'black', 'white' or '' (if there's no piece on the tile)
        """
        if self.board[pos] == ' ' or self.board[pos] == '+':
            return ''
        if self.board[pos] in self.black_pieces:
            return 'black'
        else:
            return 'white'

    # CALL AFTER MAKING SURE MOVE IS POSSIBLE!
    def make_move(self, tile_from: int, tile_to: int) -> None:
        """
        Forcingly moves a piece
        from tile_from to tile_to
        """
        # tile_to set to tile_from value, and then make tile_from empty
        self.board[tile_to] = self.board[tile_from]
        self.colorize_tile(tile_to)

        self.board[tile_from] = ' '
        self.colorize_tile(tile_from)
        pass

    def is_a_tile(self, tile: str):
        """Checks if tile is even on the board"""
        if tile in self.proper_pos:
            return True
        return False
        pass

    def move_is_safe(self, tile_from: int, tile_to: int) -> bool:
        """
        Checks whether moving from tile_from to tile_to
        is within the rules
        """
        # keep the rules basic for now
        if 0 <= tile_from < 64 and 0 <= tile_to < 64:
            return True
        else:
            return False
        pass

    def make_move_safe(self, tile_from: str | int, tile_to: str | int) -> str:
        """
        Makes a move from tile_from to tile_to.
        But only if it is within the rules!

        returns 'MoveMade' if move is made, 'MoveError' otherwise.
        """

        if isinstance(tile_from, str):
            if not self.is_a_tile(tile_from):
                return 'MoveError'
            tile_from = self.proper_pos[tile_from]
        if isinstance(tile_to, str):
            if not self.is_a_tile(tile_to):
                return 'MoveError'
            tile_to = self.proper_pos[tile_to]

        if self.move_is_safe(tile_from, tile_to):
            self.make_move(tile_from, tile_to)
            self.change_turn()
            return 'MoveMade'
        else:
            return 'MoveError'

if __name__ == '__main__':
    a = MoveMaker()
    print(a.proper_board())
