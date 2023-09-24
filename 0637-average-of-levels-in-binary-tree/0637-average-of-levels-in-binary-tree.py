# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []
        if not root:
            return avgs
        if not (root.left or root.right):
            return [root.val]
        rowSum = 0 
        rowCt = 0 
        currRow = deque([root])
        nextRow = deque()
        while currRow:
            node = currRow.popleft()
            rowSum += node.val
            rowCt += 1
            if node.left:
                nextRow.append(node.left)
            if node.right:
                nextRow.append(node.right)
            if not currRow: 
                currRow = nextRow
                nextRow = deque()
                avgs.append(rowSum / rowCt)
                rowSum = 0 
                rowCt = 0 
        return avgs