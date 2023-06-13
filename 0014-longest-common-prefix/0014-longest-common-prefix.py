class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # single element means full string is common prefix 
        if len(strs) == 1:
            return strs[0]
        # otherwise sort 
        strs.sort() # O(n)
        first = strs[0]
        last = strs[len(strs) - 1]
        prefix = ""
        for i, char in enumerate(first):
            if char == last[i]:
                prefix = prefix + char
            else:
                return prefix 
        return prefix 