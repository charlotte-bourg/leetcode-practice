class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = 0
        rMin = 1
        rMax = len(matrix) - 1 
        c = 0 
        cMin = 0
        cMax = len(matrix[0]) - 1 
        if cMax == 0:
            dir = 1
        else:
            dir = 0 
        ret = [matrix[r][c]]
        for _ in range(len(matrix) * len(matrix[0]) - 1):
            # right
            if dir == 0: 
                c += 1
                if c == cMax: 
                    dir += 1 
                    cMax -= 1 
            # down
            elif dir == 1:
                r += 1 
                if r == rMax:
                    dir += 1 
                    rMax -= 1 
            # left
            elif dir == 2:
                c -= 1
                if c == cMin:
                    dir += 1 
                    cMin += 1 
            # up
            else: 
                r -= 1
                if r == rMin:
                    dir = 0 
                    rMin += 1 
            ret.append(matrix[r][c])
        return ret 
