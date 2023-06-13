class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        ndl = len(needle)
        for i in range(0, len(haystack)-ndl+1):
            if haystack[i:i+ndl] == needle:
                return i 
        return -1