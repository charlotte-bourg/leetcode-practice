class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        print(nums)
        if not nums:
            return 0 
        lst = nums[0]
        ct = 1
        mx = ct
        for i in range(1, len(nums)):
            ct = ct+1 if nums[i] == lst+1 else 1 
            print(ct)
            if ct > mx:
                mx = ct
            lst = nums[i]
        return mx