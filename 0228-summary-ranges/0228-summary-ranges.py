class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        if l == 0:
            return []
        a = []
        s = 0 
        e = 0 
        for i in range(1, l): 
            if nums[i] == (nums[i-1]+1): 
                e = i
            else:
                if s != e: 
                    a.append(f'{nums[s]}->{nums[e]}')
                else:
                    a.append(f'{nums[s]}')
                s = i
                e = i
        if s != e: 
            a.append(f'{nums[s]}->{nums[e]}')
        else:
            a.append(f'{nums[s]}')
        return a

# [0,1,2,4,5,7]
# s = 0
# e = 0 
# i = 0 
# does nums[1] == nums[0] + 1? yes
#   e = 1
# i = 1
# does nums[2] == nums[1] + 1? yes
#   e = 2
# i = 2
# does nums[3] == nums[2] + 1? no
#   does s = e? no
#   append 0 -> 2
#   s = 3
#   e = 3 
# i = 3
# does nums[4] = nums[3] + 1? yes
#   e = 4
# i = 4 
# does nums[5] = nums[4] + 1? no
#   does s= e? no
#       append 4->5
#


# pseudocode
# given examples
# [0,1,2,4,5,7]
# whenever nums[i+1] is nums[i] + 1, include in the current range
# othersise mark as its own number 