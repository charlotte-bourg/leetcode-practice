class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set(nums) # O(n)
        nums_2 = list(set_nums)
        nums_2.sort()
        k = 0
        for num in nums_2: # O(n)
            nums[k] = num
            k += 1
        return k 