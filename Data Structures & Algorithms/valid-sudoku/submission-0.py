class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        for i in range (n):
            mark = {}
            for j in range (n):
                if board[i][j] == ".": continue
                if board[i][j] in mark:
                    return False
                mark[board[i][j]] = 1

        for j in range(n):
            mark = {}
            for i in range(n):
                if board[i][j] == ".": continue
                if board[i][j] in mark:
                    return False
                mark[board[i][j]] = 1
        
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                mark = {}
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] == ".": continue
                        if board[i + k][j + l] in mark:
                            return False
                        mark[board[i + k][j + l]] = 1
        return True