class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ') 
        if len(s) != len(pattern):
            return False
        pat_map = {}
        vals = set()
        for i, pat_key in enumerate(pattern):
            if pat_key not in pat_map: 
                if s[i] in vals: 
                    return False
                pat_map[pat_key] = s[i]
                vals.add(s[i])
            else:
                if pat_map[pat_key] != s[i]:
                    return False
        return True

# Pseudocode
# split the string s on the space character to get a list of words (strings)
# if the length of the list and the length of the pattern are not the same, return False as this is not a match
# otherwise create a hashmap (dictionary) to store a value in pattern as the key and the corresponding word in 
# s as the value
