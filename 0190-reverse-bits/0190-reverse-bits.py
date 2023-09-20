class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0 
        place = 31
        while n:
            ans += (n & 1) << place
            n = n >> 1 
            place -= 1 
        return ans 
