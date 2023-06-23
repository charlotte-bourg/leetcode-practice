class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        ai = len(a) - 1
        bi = len(b) - 1
        carry = 0 
        while ai >= 0 or bi >= 0:
            sum_pl = carry
            if ai >= 0:
                sum_pl += int(a[ai])
            if bi >= 0:
                sum_pl += int(b[bi])   
            ans = '1' + ans if sum_pl == 1 or sum_pl == 3 else '0' + ans
            carry = 1 if sum_pl == 2 or sum_pl == 3 else 0 
            ai -= 1
            bi -= 1
        if carry == 1:
            ans = '1' + ans
        return ans

