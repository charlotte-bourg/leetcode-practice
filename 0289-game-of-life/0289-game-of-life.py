class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boardCopy = [row[:] for row in board]
        for r in range(len(board)):
            for c in range(len(board[0])):
                liveNeighbors = 0
                print(f"r, c: {r}, {c}")
                if r > 0: 
                    liveNeighbors += boardCopy[r-1][c]
                    if c > 0:
                        liveNeighbors += boardCopy[r-1][c-1]
                    if c < len(board[0]) - 1:
                        liveNeighbors += boardCopy[r-1][c+1]
                if c > 0:
                    liveNeighbors += boardCopy[r][c-1]
                    if r < len(board) - 1:
                        liveNeighbors += boardCopy[r+1][c-1]
                if r < len(board) - 1:
                    liveNeighbors += boardCopy[r+1][c]
                    if c < len(board[0]) - 1:
                        liveNeighbors += boardCopy[r+1][c+1]
                if c < len(board[0]) - 1: 
                    liveNeighbors += boardCopy[r][c+1]
                if board[r][c] == 1 and (liveNeighbors < 2 or liveNeighbors > 3): 
                    board[r][c] = 0 
                elif board[r][c] == 0 and liveNeighbors == 3: 
                    board[r][c] = 1 