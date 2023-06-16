class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = len(nums)
        if end < 2:
            return len(nums) + 1
        i = 2 
        one = nums[0]
        two = nums[1]
        while i < end:
            val = nums[i]
            if val == one and one == two:
                del nums[i]
                nums.append(val)
                end -= 1 
            else:
                i += 1
                one = two
                two = val 
        return end
            
