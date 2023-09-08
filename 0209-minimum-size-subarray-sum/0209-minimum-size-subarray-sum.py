class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = 0
        slidingSum = 0
        i = 0 # first pointer
        for j in range(len(nums)):
            # at start of first loop, i = 0 and j = 0 
            # keep i <= j and j < len(nums)
            slidingSum += nums[j]
            while slidingSum >= target: # if you've slid j far enough to find a subarray where the sum is greater than or equal to target, slide i until the sum is less than target to see if there is a smaller subarray in this area
                if minSize == 0 or (j - i + 1) < minSize: 
                    minSize = j - i + 1
                slidingSum -= nums[i]
                if i == j:
                    break
                i += 1 
        return minSize