class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.transpose(matrix, n)
        self.reflect(matrix, n)

    def transpose(self, matrix, n):
        maxC = 1
        for r in range(1, n):
            for c in range(maxC):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                #print(f"swapping matrix[{r}][{c}] with matrix[{c}][{r}]")
            maxC += 1

    def reflect(self, matrix, n):
        for r in range(n):
            for c in range(n//2): # floor division operator 
                matrix[r][c], matrix[r][n-c-1] = matrix[r][n-c-1], matrix[r][c]

        

# equivalent operations to rotating clockwise: transpose across diagonal axis then reflect across vertical axis 

# transpose example operations:
# 0,0 <> n-1,n-1
# r = 0, c = 3 <> r = , c = n - c - 1 
# r = 0, c = 3 