class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid 
        islands = 0 
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1":
                    self.mapIsland(r,c)
                    islands += 1 
        return islands

    def mapIsland(self, r, c):
        self.grid[r][c] = "#"
        # up
        if r > 0 and self.grid[r-1][c] == "1":
            self.mapIsland(r-1, c)
        # down
        if r + 1 < self.rows and self.grid[r+1][c] =="1":
            self.mapIsland(r+1, c)
        # left
        if c > 0 and self.grid[r][c-1] == "1":
            self.mapIsland(r, c-1)
        # right 
        if c + 1 < self.cols and self.grid[r][c+1] =="1":
            self.mapIsland(r, c+1)


