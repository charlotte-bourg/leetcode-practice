class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        x = min(l,k)
        win = set(nums[0:x])
        if len(win) < x:
            return True
        print(win)
        for i in range(k,l):
            if nums[i] in win:
                return True
            win.add(nums[i])
            win.remove(nums[i-k])
        return False

# problem summary
# i and j such that values at those indices are the same
# and the difference between the indices is less than or equal to k 
# approach
# sliding window with a set 
# pseucode 
# add elements from 0 to k to a set
# as you're adding, check if the number is already in the set 
# siding window with set