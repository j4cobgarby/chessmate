class Piece:
    def __init__(self, colour):
        self.colour = colour # colour = 0 if white, 1 if black

    '''
    Board is a 2d list of Pieces. 
    Row 0 corresponds to row 1 on a chessboard, and
    column 0 corresponds to column A.
    '''
    def get_moves(self, board, r, c):
        return []

    def __str__(self):
        return "? "

class Board:
    def __init__(self, rows, columns):
        self.board = [[None for c in range(columns)] for r in range(rows)]

    def __str__(self):
        ret = ""
        for r in self.board:
            for p in r:
                ret += str(p) if p != None else "_ "
            ret += "\n"
        return ret

    def __getitem__(self, key):
        return self.board[key]

class Pawn:
    def __str__(self):
        return "p "

    def get_moves(self, board, r, c):
        ret = []
        if colour == 0: # Black
            if r+1 < len(board):
                ret = [(r+1, c)]
                a = board[r+1][c-1]
                b = board[r+1][c+1]

                if c-1 >= 0 and a != None and a.colour != self.colour:
                    ret.append((r+1,c-1))
                if c+1 < len(board[0]) and b != None and b.colour != self.colour:
                    ret.append((r+1,c+1))
        else: # White
            if r-1 >= 0:
                ret = [(r-1, c)]
                a = board[r-1][c-1]
                b = board[r-1][c+1]

                if c-1 >= 0 and a != None and a.colour != self.colour:
                    ret.append((r-1,c-1))
                if c+1 < len(board[0]) and b != None and b.colour != self.colour:
                    ret.append((r-1,c+1))