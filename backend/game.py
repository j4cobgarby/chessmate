class Piece:
    def __init__(self, colour, board, r, c):
        self.colour = colour  # colour = 0 if white, 1 if black
        self.board = board
        self.r = r
        self.c = c

    '''
    Board is a 2d list of Pieces. 
    Row 0 corresponds to row 1 on a chessboard, and
    column 0 corresponds to column A.
    '''

    def get_moves(self):
        return []

    def __str__(self):
        return "? "


class Board:
    def __init__(self, rows, columns):
        self.board = [[None for c in range(columns)] for r in range(rows)]

    def __str__(self):
        ret = ""
        for r in reversed(self.board):
            for p in r:
                ret += str(p) if p != None else "_ "
            ret += "\n"
        return ret

    def __getitem__(self, key):
        return self.board[key]

    def __len__(self):
        return len(self.board)

    def in_board(self, r, c):
        return r >= 0 and r < len(self.board) and c >= 0 and c < len(self.board[0])


class Pawn(Piece):
    def __str__(self):
        return "p "

    def get_moves(self):
        # Add promotion and en passant
        ret = []
        if self.colour == 1:  # White
            if self.r + 1 < len(self.board) and self.board[self.r+1][self.c] is None:
                ret = [(self.r + 1, self.c)]
                a = self.board[self.r + 1][self.c - 1]
                b = self.board[self.r + 1][self.c + 1]

                if self.c - 1 >= 0 and a is not None and a.colour != self.colour:
                    ret.append((self.r + 1, self.c - 1))
                if self.c + 1 < len(self.board[0]) and b != None and b.colour != self.colour:
                    ret.append((self.r + 1, self.c + 1))

        else:  # Black
            if self.r - 1 >= 0:
                ret = [(self.r - 1, selfc)]
                a = self.board[self.r - 1][self.c - 1]
                b = self.board[self.r - 1][self.c + 1]

                if self.c - 1 >= 0 and a is not None and a.colour != self.colour:
                    ret.append((self.r - 1, self.c - 1))
                if self.c + 1 < len(self.board[0]) and b is not None and b.colour != self.colour:
                    ret.append((self.r - 1, self.c + 1))

        return ret


class Rook(Piece):
    def __str__(self):
        return "r "

    def get_moves(self):
        valid_squares = []

        # To the right of the rook:
        if self.board.in_board(self.r, self.c + 1):
            for x in range(self.c + 1, len(self.board[0])):
                if self.board[self.r][x] is None:
                    valid_squares.append((self.r,x))
                elif self.board[self.r][x].colour != self.colour:
                    valid_squares.append((self.r,x))
                    break
                else:
                    break

        # To the left of the rook:
        if self.board.in_board(self.r, self.c - 1):
            for x in range(self.c - 1, -1, -1):
                if self.board[self.r][x] is None:
                    valid_squares.append((self.r,x))
                elif self.board[self.r][x].colour != self.colour:
                    valid_squares.append((self.r,x))
                    break
                else:
                    break

        # Above the rook:
        if self.board.in_board(self.r + 1, self.c):
            for y in range(self.r + 1, len(self.board)):
                if self.board[y][c] is None:
                    valid_squares.append((y,self.c))
                elif self.board[y][self.c].colour != self.colour:
                    valid_squares.append((y,self.c))
                    break
                else:
                    break

        # Below the rook:
        if self.board.in_board(self.r - 1, self.c):
            for y in range(r - 1, -1, -1):
                if self.board[y][self.c] is None:
                    valid_squares.append((y,self.c))
                elif self.board[y][self.c].colour != self.colour:
                    valid_squares.append((y,self.c))
                    break
                else:
                    break

        return valid_squares

class Bishop(Piece):
    def __str__(self):
        return "b "

    def get_moves(self):
        valid_squares = []

        # Up and right:
        if self.board.in_board(self.r + 1, self.c + 1):
            max_dist = min(len(self.board)-self.c, len(self.board[0])-self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r+i][self.c+i] is None:
                    valid_squares.append((self.r+i,self.c+i))
                elif self.board[self.r+i][self.c+i].colour != self.colour:
                    valid_squares.append((self.r+i,self.c+i))
                    break
                else:
                    break

        # Down and right:
        if self.board.in_board(self.r + 1, self.c - 1):
            max_dist = min(self.c, len(self.board[0])-self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r+i][self.c-i] is None:
                    valid_squares.append((self.r+i,self.c-i))
                elif self.board[self.r+i][self.c-i].colour != self.colour:
                    valid_squares.append((self.r+i,self.c-i))
                    break
                else:
                    break

        # Down and left:
        if self.board.in_board(self.r - 1, self.c - 1):
            max_dist = min(self.c, self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r-i][self.c-i] is None:
                    valid_squares.append((self.r-i,self.c-i))
                elif self.board[self.r-i][self.c-i].colour != self.colour:
                    valid_squares.append((self.r-i,self.c-i))
                    break
                else:
                    break

        # Up and left:
        if self.board.in_board(self.r - 1, self.c + 1):
            max_dist = min(len(self.board)-self.c, self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r-i][self.c+i] is None:
                    valid_squares.append((self.r-i,self.c+i))
                elif self.board[self.r-i][self.c+i].colour != self.colour:
                    valid_squares.append((self.r-i,self.c+i))
                    break
                else:
                    break

        return valid_squares

class Queen(Piece):
    def __str__(self):
        return "q "

    def get_moves(self):
        valid_squares = []

        # Right:
        if self.board.in_board(self.r, self.c + 1):
            for x in range(self.c + 1, len(self.board[0])):
                if self.board[self.r][x] is None:
                    valid_squares.append((self.r,x))
                elif self.board[self.r][x].colour != self.colour:
                    valid_squares.append((self.r,x))
                    break
                else:
                    break

        # Left:
        if self.board.in_board(self.r, self.c - 1):
            for x in range(self.c - 1, -1, -1):
                if self.board[self.r][x] is None:
                    valid_squares.append((self.r,x))
                elif self.board[self.r][x].colour != self.colour:
                    valid_squares.append((self.r,x))
                    break
                else:
                    break

        # Up:
        if self.board.in_board(self.r + 1, self.c, len(self.board), len(self.board[0])):
            for y in range(self.r + 1, len(self.board)):
                if self.board[y][self.c] is None:
                    valid_squares.append((y,self.c))
                elif self.board[y][self.c].colour != self.colour:
                    valid_squares.append((y,self.c))
                    break
                else:
                    break

        # Down:
        if self.board.in_board(self.r - 1, self.c, len(self.board), len(self.board[0])):
            for y in range(self.r - 1, -1, -1):
                if self.board[y][self.c] is None:
                    valid_squares.append((y,self.c))
                elif self.board[y][self.c].colour != self.colour:
                    valid_squares.append((y,self.c))
                    break
                else:
                    break

        # Up and right:
        if self.board.in_board(self.r + 1, self.c + 1):
            max_dist = min(len(self.board) - self.c, len(self.board[0]) - self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r + i][self.c + i] is None:
                    valid_squares.append((self.r + i, self.c + i))
                elif self.board[self.r + i][self.c + i].colour != self.colour:
                    valid_squares.append((self.r + i, self.c + i))
                    break
                else:
                    break

        # Down and right:
        if self.board.in_board(self.r + 1, self.c - 1):
            max_dist = min(self.c, len(self.board[0]) - self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r + i][self.c - i] is None:
                    valid_squares.append((self.r + i, self.c - i))
                elif self.board[self.r + i][self.c - i].colour != self.colour:
                    valid_squares.append((self.r + i, self.c - i))
                    break
                else:
                    break

        # Down and left:
        if self.board.in_board(self.r - 1, self.c - 1):
            max_dist = min(self.c, self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r - i][self.c - i] is None:
                    valid_squares.append((self.r - i, self.c - i))
                elif self.board[self.r - i][self.c - i].colour != self.colour:
                    valid_squares.append((self.r - i, self.c - i))
                    break
                else:
                    break

        # Up and left:
        if self.board.in_board(self.r - 1, self.c + 1):
            max_dist = min(len(self.board) - self.c, self.r) - 1
            for i in range(1, max_dist):
                if self.board[self.r - i][self.c + i] is None:
                    valid_squares.append((self.r - i, self.c + i))
                elif self.board[self.r - i][self.c + i].colour != self.colour:
                    valid_squares.append((self.r - i, self.c + i))
                    break
                else:
                    break

        return valid_squares

class Basilisk(Piece):
    def __str__(self):
        return "B "

    def get_moves(self):
        valid_squares = []

        if self.board.in_board(self.r + 1, self.c):
            for i in range(0,len(self.board[0])):
                if self.board[self.r+1][i] is None or self.board[self.r+1][i].colour != self.colour:
                    valid_squares.append((self.r+1,i))
                    
        if self.board.in_board(self.r - 1, self.c):
            for i in range(0,len(self.board[0])):
                if self.board[self.r-1][i] is None or self.board[self.r-11][i].colour != self.colour:
                    valid_squares.append((self.r-1,i))

        return valid_squares
