class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for r in range(self.rows):
            for c in range(self.cols):
                if self.backtrack(r, c, word):
                    return True

        return False

    def backtrack(self, r, c, suffix):
        if len(suffix) == 0:
            return True
        
        if r < 0 or r == self.rows or c < 0 or c == self.cols or self.board[r][c] != suffix[0]:
            return False
        
        ret = False
        self.board[r][c] = "."
        for rOffset, cOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(r+rOffset, c+cOffset, suffix[1:])
            if ret: 
                break
        self.board[r][c] = suffix[0]

        return ret 