class Piece:
    def __init__(self, colour):
        self.colour = colour  # colour = 0 if white, 1 if black

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

    def get_moves(self, board, r, c):
        # Add promotion and en passant
        ret = []
        if self.colour == 1:  # White
            if r + 1 < len(board) and board[r+1][c] is None:
                ret = [(r + 1, c)]
                a = board[r + 1][c - 1]
                b = board[r + 1][c + 1]

                if c - 1 >= 0 and a is not None and a.colour != self.colour:
                    ret.append((r + 1, c - 1))
                if c + 1 < len(board[0]) and b != None and b.colour != self.colour:
                    ret.append((r + 1, c + 1))

        else:  # Black
            if r - 1 >= 0:
                ret = [(r - 1, c)]
                a = board[r - 1][c - 1]
                b = board[r - 1][c + 1]

                if c - 1 >= 0 and a is not None and a.colour != self.colour:
                    ret.append((r - 1, c - 1))
                if c + 1 < len(board[0]) and b is not None and b.colour != self.colour:
                    ret.append((r - 1, c + 1))

        return ret


class Rook(Piece):
    def __str__(self):
        return "r "

    def get_moves(self, board, r, c):
        valid_squares = []

        # To the right of the rook:
        if board.in_board(r, c + 1):
            for x in range(c + 1, len(board[0])):
                if board[r][x] is None:
                    valid_squares.append((r,x))
                elif board[r][x].colour != self.colour:
                    valid_squares.append((r,x))
                    break
                else:
                    break

        # To the left of the rook:
        if board.in_board(r, c - 1):
            for x in range(c - 1, -1, -1):
                if board[r][x] is None:
                    valid_squares.append((r,x))
                elif board[r][x].colour != self.colour:
                    valid_squares.append((r,x))
                    break
                else:
                    break

        # Above the rook:
        if board.in_board(r + 1, c):
            for y in range(r + 1, len(board)):
                if board[y][c] is None:
                    valid_squares.append((y,c))
                elif board[y][c].colour != self.colour:
                    valid_squares.append((y,c))
                    break
                else:
                    break

        # Below the rook:
        if board.in_board(r - 1, c):
            for y in range(r - 1, -1, -1):
                if board[y][c] is None:
                    valid_squares.append((y,c))
                elif board[y][c].colour != self.colour:
                    valid_squares.append((y,c))
                    break
                else:
                    break

        return valid_squares

class Bishop(Piece):
    def __str__(self):
        return "b "

    def get_moves(self, board, r, c):
        valid_squares = []

        # Up and right:
        if board.in_board(r + 1, c + 1):
            max_dist = min(len(board)-c, len(board[0])-r) - 1
            for i in range(1, max_dist):
                if board[r+i][c+i] is None:
                    valid_squares.append((r+i,c+i))
                elif board[r+i][c+i].colour != self.colour:
                    valid_squares.append((r+i,c+i))
                    break
                else:
                    break

        # Down and right:
        if board.in_board(r + 1, c - 1):
            max_dist = min(c, len(board[0])-r) - 1
            for i in range(1, max_dist):
                if board[r+i][c-i] is None:
                    valid_squares.append((r+i,c-i))
                elif board[r+i][c-i].colour != self.colour:
                    valid_squares.append((r+i,c-i))
                    break
                else:
                    break

        # Down and left:
        if board.in_board(r - 1, c - 1):
            max_dist = min(c, r) - 1
            for i in range(1, max_dist):
                if board[r-i][c-i] is None:
                    valid_squares.append((r-i,c-i))
                elif board[r-i][c-i].colour != self.colour:
                    valid_squares.append((r-i,c-i))
                    break
                else:
                    break

        # Up and left:
        if board.in_board(r - 1, c + 1):
            max_dist = min(len(board)-c, r) - 1
            for i in range(1, max_dist):
                if board[r-i][c+i] is None:
                    valid_squares.append((r-i,c+i))
                elif board[r-i][c+i].colour != self.colour:
                    valid_squares.append((r-i,c+i))
                    break
                else:
                    break

        return valid_squares

class Queen(Piece):
    def __str__(self):
        return "q "

    def get_moves(self, board, r, c):
        valid_squares = []

        # Right:
        if board.in_board(r, c + 1):
            for x in range(c + 1, len(board[0])):
                if board[r][x] is None:
                    valid_squares.append((r,x))
                elif board[r][x].colour != self.colour:
                    valid_squares.append((r,x))
                    break
                else:
                    break

        # Left:
        if board.in_board(r, c - 1):
            for x in range(c - 1, -1, -1):
                if board[r][x] is None:
                    valid_squares.append((r,x))
                elif board[r][x].colour != self.colour:
                    valid_squares.append((r,x))
                    break
                else:
                    break

        # Up:
        if board.in_board(r + 1, c, len(board), len(board[0])):
            for y in range(r + 1, len(board)):
                if board[y][c] is None:
                    valid_squares.append((y,c))
                elif board[y][c].colour != self.colour:
                    valid_squares.append((y,c))
                    break
                else:
                    break

        # Down:
        if board.in_board(r - 1, c, len(board), len(board[0])):
            for y in range(r - 1, -1, -1):
                if board[y][c] is None:
                    valid_squares.append((y,c))
                elif board[y][c].colour != self.colour:
                    valid_squares.append((y,c))
                    break
                else:
                    break

        # Up and right:
        if board.in_board(r + 1, c + 1):
            max_dist = min(len(board) - c, len(board[0]) - r) - 1
            for i in range(1, max_dist):
                if board[r + i][c + i] is None:
                    valid_squares.append((r + i, c + i))
                elif board[r + i][c + i].colour != self.colour:
                    valid_squares.append((r + i, c + i))
                    break
                else:
                    break

        # Down and right:
        if board.in_board(r + 1, c - 1):
            max_dist = min(c, len(board[0]) - r) - 1
            for i in range(1, max_dist):
                if board[r + i][c - i] is None:
                    valid_squares.append((r + i, c - i))
                elif board[r + i][c - i].colour != self.colour:
                    valid_squares.append((r + i, c - i))
                    break
                else:
                    break

        # Down and left:
        if board.in_board(r - 1, c - 1):
            max_dist = min(c, r) - 1
            for i in range(1, max_dist):
                if board[r - i][c - i] is None:
                    valid_squares.append((r - i, c - i))
                elif board[r - i][c - i].colour != self.colour:
                    valid_squares.append((r - i, c - i))
                    break
                else:
                    break

        # Up and left:
        if board.in_board(r - 1, c + 1):
            max_dist = min(len(board) - c, r) - 1
            for i in range(1, max_dist):
                if board[r - i][c + i] is None:
                    valid_squares.append((r - i, c + i))
                elif board[r - i][c + i].colour != self.colour:
                    valid_squares.append((r - i, c + i))
                    break
                else:
                    break

        return valid_squares

class Basilisk(Piece):
    def __str__(self):
        return "B "

    def get_moves(self, board, r, c):
        valid_squares = []

        if board.in_board(r + 1, c):
            for i in range(0,len(board[0])):
                if board[r+1][i] is None or board[r+1][i].colour != self.colour:
                    valid_squares.append((r+1,i))
                    
        if board.in_board(r - 1, c):
            for i in range(0,len(board[0])):
                if board[r-1][i] is None or board[r-11][i].colour != self.colour:
                    valid_squares.append((r-1,i))

        return valid_squares
