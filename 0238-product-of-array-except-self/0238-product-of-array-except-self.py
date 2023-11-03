class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        l, r, ans = [1]*numsLen, [1]*numsLen, [1]*numsLen
        for i in range(1, numsLen):
            l[i] = nums[i-1] * l[i-1]
        for i in range(numsLen-2, -1, -1):
            r[i] = nums[i+1] * r[i+1]
        for i in range(numsLen):
            ans[i] = l[i] * r[i]
        return ans
