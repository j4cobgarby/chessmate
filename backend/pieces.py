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

class Pawn:
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