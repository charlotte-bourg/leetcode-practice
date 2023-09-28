class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIStoI = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIStoI[i] = max(LIStoI[i], LIStoI[j] + 1)
        return max(LIStoI)