class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1 
        d = digits[i]
        while d == 9:
            digits[i] = 0 
            if i == 0: #all 9s until the beginning, add a digit 
                digits = [1] + digits
                return digits
            i -= 1 
            d = digits[i]
        digits[i] = digits[i] + 1
        return digits
