class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0 
        e = len(nums) - 1
        while s <= e:
            if nums[s] == val and nums[e] != val:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
                continue
            elif nums[s] != val: 
                s += 1
            elif nums[e] == val:
                e -= 1
        if not nums or nums[0] == val:
            return 0 
        return e+1  