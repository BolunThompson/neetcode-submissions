DIGITS = set("123456789")

def noDot(l):
    return [v for v in l if v != "."]

nRows = 9
sqSize = nRows // 3


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
    for i in range(nRows):
        l = [r[i] for r in board]
        if invalid(l):
            return True
    return False

def invalidBoardSquares(board):
    for i in range(sqSize):
        for j in range(sqSize):
            sq = []
            for ri in range(sqSize*i, sqSize*(i + 1)):
                for rj in range(sqSize*j, sqSize*(j + 1)):
                    sq.append(board[ri][rj])
            if invalid(sq):
                return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return not (invalidBoardRows(board) or invalidBoardCols(board) or invalidBoardSquares(board))

