# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(val=nums[0])
        if len(nums) == 0:
            return None
        i = int(len(nums) / 2)
        return TreeNode(val = nums[i], left=self.sortedArrayToBST(nums[:i]), right=self.sortedArrayToBST(nums[i+1:]))