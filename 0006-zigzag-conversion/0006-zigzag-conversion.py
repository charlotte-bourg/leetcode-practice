class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        length = len(s)
        if numRows == 1:
            return s
        diff_1 = 2 * numRows - 2 
        diff_2 = 0
        for row in range(0, numRows):
            i = row 
            count = 0
            while i<length:
                ans = ans + s[i]
                if row == 0 or row == numRows - 1: # vertex rows 
                    i += diff_1 + diff_2
                else:
                    if count % 2 == 0:
                        i += diff_1
                    else:
                        i += diff_2
                    count += 1
            diff_1 -= 2
            diff_2 += 2
        return ans