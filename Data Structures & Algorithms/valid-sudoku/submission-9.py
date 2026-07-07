DIGITS = set("123456789")

def noDot(l):
    return [v for v in l if v != "."]

def invalidBoardRows(board):
    return any(invalid(l) for l in board)

def invalid(l):
    l = noDot(l)
    s = set(l)
    if len(l) != len(s):
        return True
    return not (s <= DIGITS)


# n^2 row reads
def invalidBoardCols(board):
    for i in range(len(board)):
        l = [r[i] for r in board]
        if invalid(l):
            return True
    return False

def invalidBoardSquares(board):
    split_board = []
    assert len(board) % 3 == 0
    squareSize = len(board) // 3

    for row in board:
        split_board.extend([row[:squareSize], row[squareSize: 2 * squareSize], row[2*squareSize:]])

    for i in range(squareSize):
        for j in range(squareSize):
            sq = []
            for k in range(squareSize):
                sq.extend(split_board[((squareSize * i) + k) * squareSize + j])
            print(sq)
            if invalid(sq):
                return True
    return False
            


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return not (invalidBoardRows(board) or invalidBoardCols(board) or invalidBoardSquares(board))

