local_debug = False

class MoveMaker:
    # @TODO: when you're going to make it all stored in sqlite, just make new movemakers every time
    # @TODO: and make a .get_info_to_store() method to extract board and turn to put into sqlite table
    # @TODO: Also later add deque of all the moves, and you can store basic json of moves in sqlite

    board = list('tMvWlVmTOoOoOoOo + + + ++ + + +  + + + ++ + + + pPpPpPpPRnBqKbNr')
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

    def __init__(self, board: str | list | None = None, turn: str = 'white') -> None:
        if board is not None:
            self.board = list(board)
        self.turn = turn
        pass

    def proper_board(self, for_console=False):
        """Returns a board in 8 lines, not in 1 line.
        If you set for_console to True it will divide rows by '/n',
        otherwise it will divide them by '<br />' for HTML."""
        if for_console:
            delim = '|\n'
        else:
            delim = '|<br />'
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

    def check_piece_color(self, pos: int) -> str:
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

    def check_piece(self, pos: int) -> bool:
        """
        Checks if a piece is on pos or an empty square
        """
        if self.board[pos] == ' ' or self.board[pos] == '+':
            return False
        else:
            return True

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

    def move_is_legal(self, tile_from: int, tile_to: int) -> bool:
        """
        Checks whether moving from tile_from to tile_to
        is within the rules
        """
        # makes a PieceChecker and checks legal moves
        pc = PieceChecker(tile_from, self.board, self.turn)
        if tile_to in pc.legal_moves():
            return True
        else:
            return False
        pass

    def make_move_safe(self, tile_from: str | int, tile_to: str | int) -> str:  # ######################################
        """
        Makes a move from tile_from to tile_to.
        But only if it is within the rules!

        returns 'MoveMade' if move is made, 'MoveError : {description}' otherwise.
        """

        if isinstance(tile_from, str):
            if not self.is_a_tile(tile_from):
                return 'MoveError: tile_from is not a tile'
            tile_from = self.proper_pos[tile_from]
        if isinstance(tile_to, str):
            if not self.is_a_tile(tile_to):
                return 'MoveError: tile_to is not a tile'
            tile_to = self.proper_pos[tile_to]

        piece_color = self.check_piece_color(tile_from)
        if piece_color == '':
            return 'MoveError: no piece on tile_from'
        elif piece_color != self.turn:
            return "MoveError: trying to move opponent's piece"

        if self.move_is_legal(tile_from, tile_to):
            self.make_move(tile_from, tile_to)
            self.change_turn()
            return 'MoveMade'
        else:
            return 'MoveError: illegal move'
        pass  # ########################################################################################################

# @TODO: (можно кстати на nparray'и переписать. Может быть полезно)
# для проверки того, наступает ли король на клетку, которую уже атакуют,
# можно вести два массива - атакованных клеток (один для черных,другой для белых).
# когда фигура ставится на какую-то клетку, все клетки, на которые она может встать +1,
# когда фигура уходит с этой клетки, то на всех этих клетках -1


class PieceChecker(MoveMaker):
    def __init__(self, pos: int, board: list[str], turn: str):
        """it makes an object which determines
        which piece is on the pos of the board"""
        super().__init__(board, turn)
        # I don't like that we are essentially making 3 classes per move:
        # MoveMaker -> PieceChecker (in move_is_legal method) -> NEW MoveMaker (in __init__ of PieceChecker)
        # perhaps we could make 1st and 2nd MoveMaker the same by something like

        # def __init__(self, move_maker_obj: MoveMaker):
        #     super() = move_maker_obj

        self.piece = None
        self.color = None
        self.pos = pos
        self.row = pos >> 3
        self.col = pos & 7
        tile = board[pos].lower()
        if tile == "+" or tile == "-":
            pass  # the square is empty
            return

        # Getting the piece (and its color) of the tile
        match tile:
            case "l":
                self.color = "black"
                self.piece = "king"
            case "k":
                self.color = "white"
                self.piece = "king"
            case "w":
                self.color = "black"
                self.piece = "queen"
            case "q":
                self.color = "white"
                self.piece = "queen"
            case "m":
                self.color = "black"
                self.piece = "knight"
            case "n":
                self.color = "white"
                self.piece = "knight"
            case "v":
                self.color = "black"
                self.piece = "bishop"
            case "b":
                self.color = "white"
                self.piece = "bishop"
            case "t":
                self.color = "black"
                self.piece = "rook"
            case "r":
                self.color = "white"
                self.piece = "rook"
            case "o":
                self.color = "black"
                self.piece = "pawn"
            case "p":
                self.color = "white"
                self.piece = "pawn"
        pass

    def can_delta_move(self, dx, dy):
        """Returns True if moving dx horizontally
        and dy vertically is still within the board,
        returns False otherwise"""
        return (0 <= (self.col + dx) < 8) and (0 <= (self.row + dy) < 8)

    def legal_moves(self) -> set:
        """returns all legal moves for a piece"""
        if self.piece is None or self.color != self.turn:
            # print('WTF!!!!!!!????????')
            return set()
        # print('legal_moves: getting attribute - ')  # @TODO:DELETE ---------------------------------------------REMOVE
        # print(self.__getattribute__(f"{self.color}_{self.piece}_moves")())
        # print(f"{self.color}_{self.piece}_moves")
        return self.__getattribute__(f"{self.color}_{self.piece}_moves")()

    pass

    def white_king_moves(self) -> set:
        # @TODO: добавить проверку на то атакованы ли поля и на рокировку
        ret = set()
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                if self.can_delta_move(i,j):
                    newpos = self.pos + i * 8 + j
                    ret.add(newpos)
        return ret

    def black_king_moves(self) -> set:
        return self.white_king_moves()

    def white_queen_moves(self) -> set:
        ret = set()
        right_up = True
        right = True
        right_down = True
        down = True
        left_down = True
        left = True
        left_up = True
        up = True
        for i in range(1, 8):
            # O - is where the piece is headed

            #  O
            # /
            i8 = i << 3
            if right_up:
                newpos = self.pos + i - i8
                if self.can_delta_move(i, -i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        right_up = False
                    else:
                        right_up = False
                else:
                    right_up = False

            # -O
            if right:
                newpos = self.pos + i
                if self.can_delta_move(i, 0):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        right = False
                    else:
                        right = False
                else:
                    right = False
            # \
            #  O
            if right_down:
                newpos = self.pos + i + i8
                if self.can_delta_move(i, i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        right_down = False
                    else:
                        right_down = False
                else:
                    right_down = False

            # |
            # O
            if down:
                newpos = self.pos + i8
                if self.can_delta_move(0, i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        down = False
                    else:
                        down = False
                else:
                    down = False

            #  /
            # O
            if left_down:
                newpos = self.pos - i + i8
                if self.can_delta_move(-i, i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        left_down = False
                    else:
                        left_down = False
                else:
                    left_down = False

            # O-
            if left:
                newpos = self.pos - i
                if self.can_delta_move(-i, 0):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        left = False
                    else:
                        left = False
                else:
                    left = False

            # O
            #  \
            if left_up:
                newpos = self.pos - i - i8
                if self.can_delta_move(-i, -i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        left_up = False
                    else:
                        left_up = False
                else:
                    left_up = False

            # O
            # |
            if up:
                newpos = self.pos - i8
                if self.can_delta_move(0, -i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        up = False
                    else:
                        up = False
                else:
                    up = False

        return ret

    def black_queen_moves(self) -> set:
        return self.white_queen_moves()

    def white_rook_moves(self) -> set:
        ret = set()
        right = True
        down = True
        left = True
        up = True
        for i in range(1, 8):
            # O - is where the piece is headed
            i8 = i << 3
            # -O
            if right:
                newpos = self.pos + i
                if self.can_delta_move(i, 0):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        right = False
                    else:
                        right = False
                else:
                    right = False

            # |
            # O
            if down:
                newpos = self.pos + i8
                if self.can_delta_move(0, i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        down = False
                    else:
                        down = False
                else:
                    down = False

            # O-
            if left:
                newpos = self.pos - i
                if self.can_delta_move(-i, 0):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        left = False
                    else:
                        left = False
                else:
                    left = False

            # O
            # |
            if up:
                newpos = self.pos - i8
                if self.can_delta_move(0, -i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        up = False
                    else:
                        up = False
                else:
                    up = False
        return ret

    def black_rook_moves(self) -> set:
        return self.white_rook_moves()

    def white_bishop_moves(self) -> set:
        ret = set()
        right_up = True
        right_down = True
        left_down = True
        left_up = True
        for i in range(1, 8):
            # O - is where the piece is headed

            #  O
            # /
            i8 = i << 3
            if right_up:
                newpos = self.pos + i - i8
                if self.can_delta_move(i, -i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        right_up = False
                    else:
                        right_up = False
                else:
                    right_up = False

            # \
            #  O
            if right_down:
                newpos = self.pos + i + i8
                if self.can_delta_move(i, i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        right_down = False
                    else:
                        right_down = False
                else:
                    right_down = False

            #  /
            # O
            if left_down:
                newpos = self.pos - i + i8
                if self.can_delta_move(-i, i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        left_down = False
                    else:
                        left_down = False
                else:
                    left_down = False

            # O
            #  \
            if left_up:
                newpos = self.pos - i - i8
                if self.can_delta_move(-i, -i):
                    piece_color = self.check_piece_color(newpos)
                    if piece_color == '':
                        ret.add(newpos)
                    elif piece_color != self.color:
                        ret.add(newpos)
                        left_up = False
                    else:
                        left_up = False
                else:
                    left_up = False

        return ret

    def black_bishop_moves(self) -> set:
        return self.white_bishop_moves()

    def white_knight_moves(self) -> set:
        ret = set()

        for dx, dy in [(1, 2), (1,-2), (-1, 2), (-1, -2),
                       (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            newpos = self.pos + dx + (dy << 3)
            if not self.can_delta_move(dx, dy) or self.check_piece_color(newpos) == self.color:
                continue
            else:
                ret.add(newpos)

        return ret

    def black_knight_moves(self) -> set:
        return self.white_knight_moves()

    def white_pawn_moves(self) -> set:
        # @TODO: MAKE PAWNS PROMOTE!
        # @TODO: MAKE EN PASSANT (probs after making list of moves)
        ret = set()
        forward = self.pos - 8
        double_forward = self.pos - 16
#         print(f"""==========white_pawn_moves=================:        < --------------------------------------- REMOVE
# pos {self.pos}
# forward {forward}
# double_forward {double_forward}
# self.can_delta_move(0, -1) {self.can_delta_move(0, -1)}
# self.check_piece(forward) {self.check_piece(forward)}
# col {self.col}
# row {self.row}
# ===============================================""")
        if self.can_delta_move(0, -1) and not self.check_piece(forward):
            ret.add(forward)
            if self.row == 6 and not self.check_piece(double_forward):
                ret.add(double_forward)
        if self.can_delta_move(1, -1):
            newpos = self.pos - 7
            if self.check_piece_color(newpos) == 'black':
                ret.add(newpos)
        if self.can_delta_move(-1, -1):
            newpos = self.pos - 9
            if self.check_piece_color(newpos) == 'black':
                ret.add(newpos)

        return ret

    def black_pawn_moves(self) -> set:
        # @TODO: same as white todos
        ret = set()
        forward = self.pos + 8
        double_forward = self.pos + 16
        if self.can_delta_move(0, 1) and not self.check_piece(forward):
            ret.add(forward)
            if self.row == 1 and not self.check_piece(double_forward):
                ret.add(double_forward)
        if self.can_delta_move(1, 1):
            newpos = self.pos + 9
            if self.check_piece_color(newpos) == 'white':
                ret.add(newpos)
        if self.can_delta_move(-1, 1):
            newpos = self.pos + 7
            if self.check_piece_color(newpos) == 'white':
                ret.add(newpos)
        return ret

    pass


if __name__ == '__main__':
    local_debug = True

    a = MoveMaker()

    def board_print(move=None):
        if move is not None:
            fr, to = move.split('-')
            a.make_move_safe(fr, to)
            board_print()
            return
        print(a.proper_board(for_console=True), end = '')
        print(a.turn + ' is to move\n')

    def get_legal_moves(pos, print_tiles = True):
        board = a.board
        if isinstance(pos, str):
            pos = a.proper_pos[pos]
        print(f'--------legal_moves_for {board[pos]}-------')
        a.check_piece_color(pos)
        pc = PieceChecker(pos, board, a.check_piece_color(pos))
        for i in pc.legal_moves():
            print(f'{a.proper_pos[i]} ', end = '')
        print("\n--------------------------------")



    board_print('d2-d4')
    board_print('d7-d5')
    get_legal_moves('d1')
    # board_print()
    # board_print('e2-e4')
    # board_print('d7-d5')
    # get_legal_moves('d1')
    # get_legal_moves('d8')
    # board_print('d1-h5')
    # get_legal_moves('h5')
