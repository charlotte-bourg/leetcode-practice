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