# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            toVisit = [root]
        else:
            return 0 
        nodes = 0 
        while toVisit:
            root = toVisit.pop()
            nodes += 1 
            if root.left:
                toVisit.append(root.left)
            if root.right:
                toVisit.append(root.right)
        return nodes