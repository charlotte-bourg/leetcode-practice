class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) #O(n)
        h = 0 
        for i, cit in enumerate(citations): #O(n)
            if cit < h: 
                break 
            h = max(h, min(i+1,cit))
        return h



# Pseudocode
# sort list in reverse order so that for each index, we know the author has i+1 papers with citations[i] citations or more
# iterate through the list and for each index / value pair, take the minimum of i+1 and the value citations[i]
# if that value is greater than the currently known h value, set that value as the new h value
# at the n
# test cases 
# given: 
# [3, 0, 6, 1, 5] => 3
# [1, 3, 1] => 1
# edge cases:
# [3] => 1
# [0] => 0 
