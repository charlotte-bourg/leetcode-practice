class Solution:
    from itertools import product

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        # find all border cells 
        borders = list(product([0, self.rows - 1], [0, self.cols - 1])) # corners
        borders = borders + list(product(range(1, self.rows - 1), [0, self.cols - 1])) + list(product([0, self.rows - 1], range(1, self.cols - 1))) # edges

        for (r, c) in borders:
            if board[r][c] == "O":
                self.mapRegion(r, c)
        
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == "O":
                    self.board[r][c] = "X"
                if self.board[r][c] == "#":
                    self.board[r][c] = "O"

    def mapRegion(self, r, c):
        self.board[r][c] = "#"
        # up
        if r > 0 and self.board[r-1][c] == "O": 
            self.mapRegion(r-1, c)
        # down
        if r + 1 < self.rows and self.board[r+1][c] == "O":
            self.mapRegion(r+1, c)
        # left
        if c > 0 and self.board[r][c-1] == "O":
            self.mapRegion(r, c-1)
        # right
        if c + 1 < self.cols and self.board[r][c+1] == "O":
            self.mapRegion(r, c+1)
            