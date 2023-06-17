class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: 
            return 1
        hi = x 
        lo = 0
        while True:
            mid = int((hi + lo)/2)
            sq = mid * mid 
            if sq == x or sq < x and (mid + 1) * (mid + 1) > x:
                return mid
            if sq > x: 
                hi = mid
            else:
                lo = mid