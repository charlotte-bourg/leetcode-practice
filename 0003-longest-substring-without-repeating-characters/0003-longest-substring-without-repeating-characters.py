class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = len(s)
        if sLen == 0:
            return 0 
        maxLen = 1
        i = 0 
        letters = set()
        for j in range(sLen):
            if s[j] not in letters: 
                letters.add(s[j])
                maxLen = max(maxLen, j - i + 1)
            else:
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        break 
                    letters.remove(s[i])
                    i += 1
        return maxLen

