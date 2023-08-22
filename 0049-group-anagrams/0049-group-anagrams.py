class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {}
        ret = []
        for s in strs: 
            alph = ''.join(sorted(list(s)))
            if alph in grps:
                grps[alph].append(s) 
            else:
                grps[alph] = [s] 
        for grp in grps.values(): 
            ret.append(grp)
        return ret 


# Pseudocode
# iterate through the list of strings and sort the characters in each word into alphabetical order
# use alpha ordered versions of words as keys and original strings as elements in a list as a corresponding value
# in a dictionary
# if that alpha sorted string is in the dictionary already, get the value (list) and append the new word
# else create a key with a value of a list with 1 element, the word
# add all values in that dictionary to a list and return the list

# overall first loop is O(n * m * log(m))