class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # O(n)
        nums = list(nums) # O(n)
        nums.sort() # O(nlogn)
        if not nums:
            return 0 
        lst = nums[0]
        ct = 1
        mx = ct
        for i in range(1, len(nums)): # O(n)
            ct = ct+1 if nums[i] == lst+1 else 1 
            if ct > mx:
                mx = ct
            lst = nums[i]
        return mx