class Solution:
    def climbStairs(self, n: int) -> int:
        val1 = 0 
        val2 = 1
        for i in range(n):
            curr = val1 + val2
            val1 = val2
            val2 = curr
        return curr
# n = 1
# 1 
# ways = 1

# n = 2
# ways = 2
# 1 1
# 2

# n = 3
# ways = 3 
# 1 1 1
# 2 1 
# 1 2 

# n = 4
# ways = 5 
# 1 1 1 1 
# 2 1 1 
# 1 2 1 
# 1 1 2 
# 2 2 

# n = 5
# ways =  8 
# 1 1 1 1 1  
# 2 1 1 1 
# 1 2 1 1
# 1 1 2 1 
# 1 1 1 2
# 2 2 1 
# 2 1 2 
# 1 2 2 

# n = 6
# ways = 13 
# 1 1 1 1 1 1 
# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1
# 1 1 1 2 1
# 1 1 1 1 2
# 2 2 1 1 
# 2 1 2 1 
# 2 1 1 2
# 1 2 2 1 
# 1 2 1 2 
# 1 1 2 2
# 2 2 2 

# rote that the number of ways for a given value of n is the nth value of a 
# fibonacci sequence starting with 1 as the 0th value
