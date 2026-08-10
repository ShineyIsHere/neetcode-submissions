class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}
        for i in range(len(board)):
            row[i] = []
            for j in range(len(board)):
                if j not in col:
                    col[j] = []
                if (i//3)*3 + j//3 not in box:
                    box[(i/3)*3 + j/3] = []
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[(i//3)*3 + j//3]:
                    return False
                elif board[i][j].isnumeric():
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[(i//3)*3 + j//3].append(board[i][j])
        return True
                
                    