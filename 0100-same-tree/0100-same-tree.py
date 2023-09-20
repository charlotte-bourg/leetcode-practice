# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False 
        pToVisit, qToVisit = [p], [q]
        while pToVisit:
            pCurr = pToVisit.pop()
            qCurr = qToVisit.pop()
            if pCurr.left or qCurr.left: 
                if (pCurr.left and not qCurr.left) or (qCurr.left and not pCurr.left) or (pCurr.left.val != qCurr.left.val):
                    return False
                pToVisit.append(pCurr.left)
                qToVisit.append(qCurr.left)
            if pCurr.right or qCurr.right:
                if (pCurr.right and not qCurr.right) or (qCurr.right and not pCurr.right) or (pCurr.right.val != qCurr.right.val):
                    return False
                if pCurr.right and qCurr.right:
                    pToVisit.append(pCurr.right)
                    qToVisit.append(qCurr.right)
        return True
