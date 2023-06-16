class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mv = k % len(nums) # num elements to move
        if mv > 0:
            mv_lst = nums[-mv:] # list of elements to move
            del nums[-mv:]
            nums[0:0] = mv_lst