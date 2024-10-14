# from select import select
# from collections import deque

local_debug = False


def dbg(s: str):
    if local_debug:
        print(f'\033[91mDEBUG\033[0m: {s}')


# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

"""Utils"""
is_queen = lambda x: x == 'w' or x == 'q'
is_bishop = lambda x: x == 'v' or x == 'b'
is_rook = lambda x: x == 't' or x == 'r'
is_knight = lambda x: x == 'm' or x == 'n'
is_king = lambda x: x == 'l' or x == 'k'
is_pawn = lambda x: x == 'o' or x == 'p'

"""MoveMaker"""

#       ?????????????????????? SHOULD I DO CHECKS?????????????????
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
        "black_king": 'l',
        "black_queen": 'w',
        "black_knight": 'm',
        "black_bishop": 'v',
        "black_rook": 't',
        "black_pawn": 'o',

        "white_king": 'k',
        "white_queen": 'q',
        "white_knight": 'n',
        "white_bishop": 'b',
        "white_rook": 'r',
        "white_pawn": 'p'
    }

    black_pieces = {'l', 'L', 'w', 'W', 'm', 'M', 'v', 'V', 't', 'T', 'o', 'O'}
    white_pieces = {'k', 'K', 'q', 'Q', 'n', 'N', 'b', 'B', 'r', 'R', 'p', 'P'}
    original_places = {
        'white_rook_left': 56, 'white_rook_right': 63, 'black_rook_left': 0, 'black_rook_right': 7,
        'white_knight_left': 57, 'white_knight_right': 62, 'black_knight_left': 1, 'black_knight_right': 6,
        'white_bishop_left': 58, 'white_bishop_right': 61, 'black_bishop_left': 2, 'black_bishop_right': 5,
        'white_queen': 59, 'white_king': 60, 'black_queen': 3, 'black_king': 4
    }
    kings = {'black': 4, 'white': 60}
    unmoved_pieces = {'white_rook_left', 'white_rook_right', 'black_rook_left',
                      'black_rook_right', 'white_king', 'black_king'}

    def __init__(self, board: str | list[str] | None = None,
                 turn: str = 'white',
                 kings=None,
                 unmoved_pieces=None,
                 prev_moves: list[str] = None
                 ) -> None:
        if prev_moves is None:
            prev_moves = []
        self.prev_moves = prev_moves
        # We store moves like this {from}-{to}|{param1}|{param2}|... or 'O-O-O' or 'O-O'
        # params could be:
        # x{piece} - piece taken from {to},  # for now we store pieces like 'P' or 'o'
        # p{piece} - piece taken by en passant,
        # m{piece} - first time moving piece # for now we store it as 'black_rook_left' or 'white_king'
        # @TODO:  I think it's better to store short versions of pieces like: wrl for white_rook_left
        # @TODO:  or even better we can store them as numbers having dictionary of correspondence
        # @TODO:  We can also add check this way and track it in self.prev_moves (if I decide to add checks)
        # We could get the board by previous moves, just doing one after the other. Maybe do it so you
        # could __init__ with board={board}|None, prev_moves = {list_of_moves} and it plays the moves one by one,
        # getting to needed position. It could be interesting, but not needed immediately
        if kings is None:
            kings = self.kings.copy()
        self.kings = kings
        if unmoved_pieces is None:
            unmoved_pieces = self.unmoved_pieces.copy()
        self.unmoved_pieces = unmoved_pieces
        if board is None:
            self.board = self.board.copy()
        elif isinstance(board, list):
            self.board = board
        else:
            self.board = list(board)
        self.turn = turn
        self.pc = None

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
            i8 = i * 8
            ret += ('|' +
                    self.board[i8] +
                    self.board[i8 + 1] +
                    self.board[i8 + 2] +
                    self.board[i8 + 3] +
                    self.board[i8 + 4] +
                    self.board[i8 + 5] +
                    self.board[i8 + 6] +
                    self.board[i8 + 7] +
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
        if (row + col) & 1 == 0:  # if (row+col) % 2 == 0 - WHITE
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
        pass

    def check_piece(self, pos: int) -> bool:
        """
        Checks if a piece is on pos or an empty square
        """
        if self.board[pos] == ' ' or self.board[pos] == '+':
            return False
        else:
            return True
        pass

    # CALL AFTER MAKING SURE MOVE IS POSSIBLE!
    def make_move(self, tile_from: int, tile_to: int) -> None:
        """
        Forcingly moves a piece
        from tile_from to tile_to
        :returns: None
        """
        # tile_to set to tile_from value, and then make tile_from empty
        clr = self.check_piece_color(tile_from)
        piece = self.board[tile_from].lower()
        if is_king(piece):
            self.kings[clr] = tile_to
            if clr + '_king' in self.unmoved_pieces:
                self.unmoved_pieces.remove(clr + '_king')
        elif is_rook(piece):
            rook_left = clr + '_rook_left'
            rook_right = clr + '_rook_right'
            if rook_left in self.unmoved_pieces and tile_from == self.original_places[rook_left]:
                self.unmoved_pieces.remove(rook_left)
            elif rook_right in self.unmoved_pieces and tile_from == self.original_places[rook_right]:
                self.unmoved_pieces.remove(rook_right)

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
        is within the rules NOT THINKING ABOUT CHECKS!
        """
        self.pc = PieceChecker(tile_from, self)
        if tile_to in self.pc.legal_moves():
            return True
        else:
            return False
        pass

    def make_move_safe(self, tile_from: str | int, tile_to: str | int) -> str:  # ######################################
        """
        Makes a move from tile_from to tile_to.
        But only if it is within the rules!
        Also writes the move down in self.prev_moves
        :returns: 'MoveMade' if move is made, 'MoveError : {description}' otherwise.
        """
        # @TODO: Perhaps, moving there_is_check into MoveMaker class would cut memory usage. Think about it...
        # Tile conversion
        if isinstance(tile_from, str):
            if not self.is_a_tile(tile_from):
                return 'MoveError: tile_from is not a tile'
            tile_from = self.proper_pos[tile_from]
        if isinstance(tile_to, str):
            if not self.is_a_tile(tile_to):
                return 'MoveError: tile_to is not a tile'
            tile_to = self.proper_pos[tile_to]

        # Checking the tiles
        piece_color = self.check_piece_color(tile_from)
        if piece_color == '':
            return 'MoveError: no piece on tile_from'
        elif piece_color != self.turn:
            return "MoveError: trying to move opponent's piece"

        # Checking if you can actually move and PERFORMING THE MOVE
        if self.move_is_legal(tile_from, tile_to):
            tile_to_piece = self.board[tile_to]
            king_is_being_moved = (tile_from == self.kings[self.turn])
            left_rook_first_move = (self.turn + '_rook_left' in self.unmoved_pieces) and (
                    tile_from == self.original_places[self.turn + '_rook_left'])
            right_rook_first_move = (self.turn + '_rook_right' in self.unmoved_pieces) and (
                    tile_from == self.original_places[self.turn + '_rook_right'])
            king_first_move = (tile_from == self.kings[self.turn]) and ((self.turn + '_king') in self.unmoved_pieces)
            # Castling movement management:
            if king_is_being_moved:
                ooo = (tile_to == (self.kings[self.turn] - 2))
                oo = (tile_to == (self.kings[self.turn] + 2))
                col = tile_from & 7
                if ooo:
                    rook_pos = tile_from - col
                    if self.pc.there_is_check(tile_from - 1) and self.pc.there_is_check(tile_from - 2):
                        return "MoveError: can't move in check during O-O-O"
                    else:
                        self.make_move(tile_from, tile_to)
                        self.make_move(rook_pos, tile_to + 1)
                        self.change_turn()
                        self.prev_moves.append('O-O-O')
                        return 'MoveMade'
                elif oo:
                    rook_pos = tile_from - col + 7
                    if self.pc.there_is_check(tile_from + 1) and self.pc.there_is_check(tile_from + 2):
                        return "MoveError: can't move in check during O-O"
                    else:
                        self.make_move(tile_from, tile_to)
                        self.make_move(rook_pos, tile_to - 1)
                        self.change_turn()
                        self.prev_moves.append('O-O')
                        return 'MoveMade'

            # Regular moves
            self.make_move(tile_from, tile_to)
            if self.pc.there_is_check(self.kings[self.turn]):
                self.make_move(tile_to, tile_from)
                # Returning pieces in unmoved set could be done smarter than three ifs,
                # but because we only track rooks and kings, I will kep it that way
                if king_is_being_moved:
                    self.unmoved_pieces.add(self.turn + '_king')
                elif left_rook_first_move:
                    self.unmoved_pieces.add(self.turn + '_rook_left')
                elif right_rook_first_move:
                    self.unmoved_pieces.add(self.turn + '_rook_right')
                self.board[tile_to] = tile_to_piece
                return "MoveError: the king mustn't be endangered"

            # Writing the move down
            the_move = self.proper_pos[tile_from] + '-' + self.proper_pos[tile_to]
            if left_rook_first_move: the_move += f"|m{self.turn}_rook_left"
            if right_rook_first_move: the_move += f"|m{self.turn}_rook_right"
            if king_first_move: the_move += f"|m{self.turn}_king"
            if tile_to_piece != ' ' and tile_to_piece != '+': the_move += f"|x{tile_to_piece}"
            self.prev_moves.append(the_move)
            self.change_turn()
            return 'MoveMade'
        else:
            return 'MoveError: illegal move'
        pass  # ########################################################################################################

    def revert_last_move(self):
        """Reverts the last move changing the board and modifying self.kings and self.unmoved_pieces accordingly"""
        if len(self.prev_moves) == 0:
            dbg('revert_last_move: No moves to revert')
            return
        last_move = self.prev_moves.pop().split('|')
        dbg(f"revert_last_move: last_move={last_move}")
        self.change_turn()
        if last_move[0] == 'O-O' or last_move[0] == 'O-O-O':
            isOO = 2 * int(last_move[0] == 'O-O') - 1
            king_place = self.original_places[self.turn + '_king']
            side = 'right' if isOO == 1 else 'left'
            self.make_move(king_place + isOO + isOO, king_place)
            self.make_move(king_place + isOO, king_place + isOO + isOO + isOO)
            self.unmoved_pieces.add(self.turn + '_king')
            self.unmoved_pieces.add(self.turn + '_rook_' + side)
            return
        fr, to = map(self.proper_pos.__getitem__, last_move[0].split('-'))
        self.make_move(to, fr)
        for i in range(1, len(last_move)):
            param = last_move[i]
            match param[0]:
                case 'm':
                    self.unmoved_pieces.add(param[1:])
                case 'x':
                    self.board[to] = param[1]
                case 'p':
                    # @TODO: EN PASSANT MANAGEMENT!
                    pass


# @TODO: (можно кстати на nparray'и переписать. Может быть полезно)


class PieceChecker(MoveMaker):
    """Pass pos into PieceChecker and you can check
    for legal moves on the board for that piece (does not check for checks in legal_moves method)"""

    def __init__(self, pos: int, move_maker: MoveMaker):
        """it makes an object which determines
        which piece is on the pos of the board
        :param pos: is int
        :param move_maker: is a MoveMaker object from which you create PieceChecker object
        """
        super().__init__(move_maker.board, move_maker.turn, move_maker.kings, move_maker.unmoved_pieces,
                         move_maker.prev_moves)
        # I don't like that we are essentially making 3 classes per move:
        # MoveMaker -> PieceChecker (in move_is_legal method) -> NEW MoveMaker (in __init__ of PieceChecker)
        # perhaps we could make 1st and 2nd MoveMaker the same by just storing self.move_maker in PieceChecker
        # and overloading __get_attribute__ method so that if attribute is not a part of PieceChecker, then it goes to
        # self.move_maker's attribute. And PieceChecker class can have move_maker set to MoveMaker class by default

        self.piece = None
        self.color = None
        self.pos = pos
        self.row = pos >> 3
        self.col = pos & 7
        tile = move_maker.board[pos].lower()
        if tile == "+" or tile == " ":
            pass  # the square is empty
            dbg(f'! PieceChecker: {pos} {move_maker.board[pos]} - not a piece')
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
        dbg(f"PieceChecker(): row={self.row}, col={self.col}, pos={self.pos}, turn={self.turn}, piece={self.color} {self.piece}")
        pass

    def can_delta_move(self, dx, dy):
        """Returns True if moving dx horizontally
        and dy vertically is still within the board,
        returns False otherwise"""
        return (0 <= (self.col + dx) < 8) and (0 <= (self.row + dy) < 8)

    def legal_moves(self) -> set:
        """returns all legal moves for a piece"""
        if self.piece is None or self.color != self.turn:
            dbg(f'legal_moves(): No piece or wrong color')
            return set()
        dbg(f'legal_moves(): self.{self.color}_{self.piece}_moves')
        return self.__getattribute__(f"{self.color}_{self.piece}_moves")()

    pass

    def there_is_check(self, pos: int | str) -> bool:
        """
        returns True if the field is a check for a king of self.color
        color if it was on pos position, False otherwise.
        If you use it to check for king moves, remove king first
        """
        if isinstance(pos, str):
            pos = self.proper_pos[pos]

        dbg(f'there_is_check({pos}): {self.color}')
        row = pos >> 3
        col = pos & 7
        right_up = True
        right = True
        right_down = True
        down = True
        left_down = True
        left = True
        left_up = True
        up = True
        "Queen | Rook | Bishop"
        for i in range(1, 8):
            # O - is where the piece is headed

            #  O
            # /
            i8 = i << 3
            if right_up:
                newpos = pos + i - i8
                if (0 <= (col + i) < 8) and (0 <= (row - i) < 8):
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_bishop(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        right_up = False
                else:
                    right_up = False

            # -O
            if right:
                newpos = pos + i
                if 0 <= (col + i) < 8:
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_rook(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        right = False
                else:
                    right = False

            # \
            #  O
            if right_down:
                newpos = pos + i + i8
                if (0 <= (col + i) < 8) and (0 <= (row + i) < 8):
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_bishop(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        right_down = False
                else:
                    right_down = False

            # |
            # O
            if down:
                newpos = pos + i8
                if 0 <= (row + i) < 8:
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_rook(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        down = False
                else:
                    down = False

            #  /
            # O
            if left_down:
                newpos = pos - i + i8
                if (0 <= (col - i) < 8) and (0 <= (row + i) < 8):
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_bishop(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        left_down = False
                else:
                    left_down = False

            # O-
            if left:
                newpos = pos - i
                if 0 <= (col - i) < 8:
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_rook(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        left = False
                else:
                    left = False

            # O
            #  \
            if left_up:
                newpos = pos - i - i8
                if (0 <= (col - i) < 8) and (0 <= (row - i) < 8):
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_bishop(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        left_up = False
                else:
                    left_up = False

            # O
            # |
            if up:
                newpos = pos - i8
                if 0 <= (row - i) < 8:
                    piece_color = self.check_piece_color(newpos)
                    tile = self.board[newpos].lower()
                    if (is_queen(tile) or is_rook(tile)) and self.color != piece_color:
                        return True
                    elif tile == ' ' or tile == '+':
                        pass
                    else:
                        up = False
                else:
                    up = False

        "Knight"
        for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            newpos = pos + dx + (dy << 3)
            if ((0 <= (col + dx) < 8) and (0 <= (row + dy) < 8)
                    and is_knight(self.board[newpos].lower())
                    and self.check_piece_color(newpos) != self.color):
                return True

        "King"
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                if (0 <= (col + i) < 8) and (0 <= (row + j) < 8):
                    newpos = pos + i + (j << 3)
                    tile = self.board[newpos].lower()
                    if is_king(tile) and self.color != self.check_piece_color(newpos):
                        return True

        "Pawn"
        dy = -1 if self.color == 'white' else 1
        # print(dy)
        if 0 <= (row + dy) < 8:
            newpos = pos + (dy << 3) + 1
            if (0 < (col + 1) < 8) and is_pawn(self.board[newpos].lower()
                                               ) and self.color != self.check_piece_color(newpos):
                return True
            newpos = pos + (dy << 3) - 1
            if (0 < (col - 1) < 8) and is_pawn(self.board[newpos].lower()
                                               ) and self.color != self.check_piece_color(newpos):
                return True
        return False
        pass

    def white_king_moves(self) -> set:
        """Does not check for checks!"""
        ret = set()
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                newpos = self.pos + (j << 3) + i
                # dbg(f'white_king_moves(): i={i} j={j}')
                if (i != 0 or j != 0) and self.can_delta_move(i, j) and self.color != self.check_piece_color(newpos):
                    ret.add(newpos)
                    # dbg(f'added {newpos}')
        dbg(f"{self.color}_king_moves ({self.pos}={self.proper_pos[self.pos]}): ")
        king_unmoved = ((self.color + '_king') in self.unmoved_pieces)
        dbg(f"king_unmoved = {king_unmoved}")
        if king_unmoved and not self.there_is_check(self.pos):
            tile1 = self.board[self.pos + 1]
            tile2 = self.board[self.pos + 2]
            rook_unmoved = ((self.color + '_rook_right') in self.unmoved_pieces)
            if (tile1 == ' ' or tile1 == '+') and (tile2 == ' ' or tile2 == '+') and rook_unmoved:
                ret.add(self.pos + 2)
            tile1 = self.board[self.pos - 1]
            tile2 = self.board[self.pos - 2]
            tile3 = self.board[self.pos - 3]
            rook_unmoved = ((self.color + '_rook_left') in self.unmoved_pieces)
            dbg(f"rook_unmoved (OOO) = {rook_unmoved}, \ntile1: {(tile1 == ' ' or tile1 == '+')}\t tile2: {(tile2 == ' ' or tile2 == '+')}\t tile3 {(tile3 == ' ' or tile3 == '+')} ")
            if ((tile1 == ' ' or tile1 == '+') and (tile2 == ' ' or tile2 == '+')
                    and (tile3 == ' ' or tile3 == '+') and rook_unmoved):
                ret.add(self.pos - 2)
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

        for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2),
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
        # print(f"""==========white_pawn_moves=================:        < --------------------------------------- REMOVE
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

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


    # local_debug = True

    a = MoveMaker()


    def board_print(the_move=None):
        move(the_move, True)


    def move(the_move=None, do_print=False):
        if the_move is not None:
            fr, to = the_move.split('-')
            print(a.make_move_safe(fr, to), f"| {bcolors.UNDERLINE + the_move + bcolors.ENDC}")
        if do_print:
            print(a.proper_board(for_console=True), end='')
            print(a.turn + ' is to move\n')


    def get_legal_moves(pos):
        board = a.board
        if isinstance(pos, str):
            pos = a.proper_pos[pos]
        print(f'--------legal_moves_for {board[pos]}-------')
        a.check_piece_color(pos)
        pc = PieceChecker(pos, a)
        for i in pc.legal_moves():
            # print(i)
            print(f'{a.proper_pos[i]} ', end='')
        print("\n--------------------------------")


    def highlight_checks(color='white'):
        print('CHECKS for ' + color + ':')
        pc = PieceChecker(a.kings[color], a)
        ret = '|'
        newret = ''
        for i in range(64):
            if i % 8 == 0 and i != 0:
                ret += newret + '|\n'
                newret = '|'
            if pc.there_is_check(i):
                newret += bcolors.FAIL + bcolors.UNDERLINE + a.board[i] + bcolors.ENDC + bcolors.ENDC
            else:
                newret += a.board[i]
        ret += newret + '|\n'
        print(ret)


    move('e2-e4')
    move('e7-e5')
    move('g1-f3')
    move('g8-f6')
    move('f1-e2')
    move('f8-e7')
    board_print('e1-g1')
    a.revert_last_move()
    print(a.prev_moves)
    board_print()
