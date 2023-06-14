class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_nums = len(nums)
        if num_nums == 1:
            return nums[0]
        nums.sort()
        lst = nums[0]
        count = 1 
        for i in range(1, num_nums):
            if nums[i] == lst:
                count += 1 
                if count > num_nums / 2:
                    return lst
            else:
                lst = nums[i]
                count = 1