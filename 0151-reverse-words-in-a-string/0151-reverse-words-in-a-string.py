class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev = ""
        for word in words:
            if not rev:
                rev = word
            else:
                rev = word + " " + rev 
        return rev