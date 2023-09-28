class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + int((high - low) / 2) # floor -> if low and high are 1 apart, mid will never become high
            # print(f"{low} {mid} {high}")
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1  
            else: 
                low = mid + 1 
        return low 