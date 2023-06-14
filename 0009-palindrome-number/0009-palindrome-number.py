class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        s = 0
        e = len(x)-1
        while s < e:
            if x[s] != x[e]:
                return False
            s = s + 1
            e = e - 1
        return True
