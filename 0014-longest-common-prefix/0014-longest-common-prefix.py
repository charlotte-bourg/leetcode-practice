class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # for i, char in enumerate(str[0]):
        #     for str[0]
        if len(strs) == 1:
            return strs[0]
        # if there is more than one element in the list
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
        # check if whole string at strs[0] matches 

