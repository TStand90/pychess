import sys


class Board:

    def __init__(self, width, height, pieces=[]):
        self.width = width
        self.height = height
        self.x_spaces = [str(unichr(x + 97)) for x in range(width)]
        self.y_spaces = range(1, height + 1)
        self.pieces = pieces


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.in_check = False
        self.checkmated = False


class Piece:

    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_position(self):
        '''
        Take a string representation of a position and return it's tuple.
        '''
        x_position = self.position[0]
        y_position = self.position[1]

        return (x_position, y_position)

    def move(self, new_position):
        original_x, original_y = self.get_position(self.position)
        new_x, new_y = self.get_position(new_position)

        if self.is_valid_move(original_x, original_y, new_x, new_y):
            self.position = new_position
            if not self.has_moved:
                self.has_moved = True
        else:
            return "Error"


class Pawn(Piece):

    def __init__(self, color, position, has_moved):
        self.color = color
        self.position = position
        self.has_moved = False

    def is_valid_move(self, original_x, original_y, new_x, new_y):
        if original_y == new_y:
            # Vertical move
            if self.is_blocked(original_x, original_y, new_x, new_y):
                return False

            if self.color == 'White':
                if original_x = new_x + 1:
                    return True
                elif (original_x=new_x+2) and not self.has_moved:
                    return True
                else:
                    return False
            else:
                if original_x = new_x - 1:
                    return True
                elif (original_x=new_x-2) and not self.has_moved:
                    return True
                else:
                    return False
        else:
            # Taking move
            pass

    def is_blocked(self, original_x, original_y, new_x, new_y):
        '''
        Pawns are only blocked on vertical moves.  On a taking move, the Pawn
        only moves one space, so blocking logic does not apply.
        '''
        pass


class King(Piece):

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False


class Queen(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False


def setup_normal_game_board():

    black_pawn_1 = Pawn('Black', 'a7')
    black_pawn_2 = Pawn('Black', 'b7')
    black_pawn_3 = Pawn('Black', 'c7')
    black_pawn_4 = Pawn('Black', 'd7')
    black_pawn_5 = Pawn('Black', 'e7')
    black_pawn_6 = Pawn('Black', 'f7')
    black_pawn_7 = Pawn('Black', 'g7')
    black_pawn_8 = Pawn('Black', 'h7')
    black_rook_1 = Rook('Black', 'a8')
    black_rook_2 = Rook('Black', 'h8')
    black_knight_1 = Knight('Black', 'b8')
    black_knight_2 = Knight('Black', 'g8')
    black_bishop_1 = Bishop('Black', 'c8')
    black_bishop_2 = Bishop('Black', 'f8')
    black_queen = Queen('Black', 'd8')
    black_king = King('Black', 'e8')

    white_pawn_1 = Pawn('White', 'a2')
    white_pawn_2 = Pawn('White', 'b2')
    white_pawn_3 = Pawn('White', 'c2')
    white_pawn_4 = Pawn('White', 'd2')
    white_pawn_5 = Pawn('White', 'e2')
    white_pawn_6 = Pawn('White', 'f2')
    white_pawn_7 = Pawn('White', 'g2')
    white_pawn_8 = Pawn('White', 'h2')
    white_rook_1 = Rook('White', 'a8')
    white_rook_2 = Rook('White', 'h8')
    white_knight_1 = Knight('White', 'b8')
    white_knight_2 = Knight('White', 'g8')
    white_bishop_1 = Bishop('White', 'c8')
    white_bishop_2 = Bishop('White', 'f8')
    white_queen = Queen('White', 'd8')
    white_king = King('White', 'e8')

    pieces = [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
              black_pawn_5, black_pawn_6, black_pawn_7, black_pawn_8,
              black_rook_1, black_rook_2, black_knight_1, black_knight_2,
              black_bishop_1, black_bishop_2, black_queen, black_king,
              white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4,
              white_pawn_5, white_pawn_6, white_pawn_7, white_pawn_8,
              white_rook_1, white_rook_2, white_knight_1, white_knight_2,
              white_bishop_1, white_bishop_2, white_queen, white_king]

    board = Board(8, 8, pieces)

    return board


def main():

    board = setup_normal_game_board()


if __name__ == '__main__':
    main()
