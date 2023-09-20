# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        toVisit = [(1, root)]
        maxDepth = 0 
        while toVisit:
            curr = toVisit.pop()
            currDepth = curr[0]
            currNode = curr[1]
            maxDepth = max(maxDepth, currDepth)
            if currNode.left:
                toVisit.append((currDepth + 1, currNode.left))
            if currNode.right:
                toVisit.append((currDepth + 1, currNode.right))
        return maxDepth 