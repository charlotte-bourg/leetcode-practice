class Solution:
    def boxesHelper(self, board, j):
        for i in range(0,3):
            digit = board[i][j]
            if digit != ".":
                if digit in chk:
                    return False
                chk.add(digit)
        for i in range(3,6):
            digit = board[i][j]
            if digit != ".":
                if digit in chk:
                    return False
                chk.add(digit)
        for i in range(6,9):
            digit = board[i][j]
            if digit != ".":
                if digit in chk:
                    return False
                chk.add(digit)
        return True
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal
        for line in board:
            chk = set()
            for digit in line:
                if digit != ".":
                    if digit in chk:
                        return False
                    chk.add(digit)
        # vertical
        for j in range(0,9): 
            chk = set()
            for i in range(0,9):
                digit = board[i][j]
                if digit != ".":
                    if digit in chk:
                        return False
                    chk.add(digit)
        # boxes
        boxes = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
        [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
        [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
        [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
        [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
        [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
        [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
        [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
        [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)],
        ]
        for box in boxes:
            chk = set()
            for coordTuple in box:
                digit = board[coordTuple[0]][coordTuple[1]]
                if digit != ".":
                    if digit in chk:
                        return False
                    chk.add(digit)
        return True