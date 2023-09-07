# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        toVisit = [root]
        while toVisit:
            curr = toVisit.pop()
            if curr:
                vals.append(curr.val)
                toVisit.append(curr.left)
                toVisit.append(curr.right)
        vals.sort()
        minDiff = vals[1] - vals[0]
        for i in range(1, len(vals)):
            minDiff = min([minDiff, vals[i] - vals[i-1]])
        return minDiff

        