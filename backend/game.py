def in_board(r,c,rows,columns):
    if a >= 0 and a <= c and b >= 0 and b <= r:
        return True
    return False

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
        if self.colour == 0: # Black
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
    
class Rook:
    def __str__(self):
        return "r "

    def get_moves(self, board, r, c):
        ret = []

        # To the right of the rook:
        if in_board(r, c+1, len(board), len(board[0])) == True:
            for x range(c+1,len(board[0])):
                if board[r][x] == None:
                    ret.append(square[r][x])
                elif board[r][x].colour != self.colour:
                    ret.append(square[r][x])
                    break
                else:
                    break

        # To the left of the rook:
        if in_board(r, c-1, len(board), len(board[0])) == True:
            for x in range(c,0,-1):
                if board[r][x] == None:
                    ret.append(square[r][x])
                elif board[r][x].colour != self.colour:
                    ret.append(square[r][x])
                    break
                else:
                    break

        # Above the rook:
        if in_board(r+1, c, len(board), len(board[0])) == True:
            for y in range(r+1,len(board)):
                if board[y][c] == None:
                    ret.append(square[y][c])
                elif board[y][c].colour != self.colour:
                    ret.append(square[y][c])
                    break
                else:
                    break

        # Below the rook:
        if in_board(r-1, c, len(board), len(board[0])) == True:
            for y in range(r-1,0,-1):
                if board[y][c] == None:
                    ret.append(square[y][c])
                elif board[y][c].colour != self.colour:
                    ret.append(square[y][c])
                    break
                else:
                    break