class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        l = len(words)
        if l == 0:
            return ans
        s = 0 # index of starting word for the given line 
        e = 0 # index of ending word for the given line
        while e < l:
            ln = ""
            lnChars = 0 
            while e < l and (maxWidth >= (lnChars + len(words[e]) + e - s)): # find end index by quitting if e hits end or if the length of the next word plus required spaces will tip over the maxWidth
                lnChars += len(words[e]) # track length of words (no spaces) in line
                e += 1 
            if e == l or (e-s) == 1: # for last line or case where there's 1 word, left justify then fill line
                base = 1
                extra = 0 
            else: 
                slots = e - s - 1 # number of slots between words
                sp = maxWidth - lnChars # spaces to allocate to those slots
                base = floor(sp/slots) # min number of spaces in each slot
                extra = sp % slots # number of slots that will have 1 extra space (greedy loading at front)
            for i in range(s, e-1):
                ln += f'{words[i]}' + base * " "
                if (i-s) < extra:
                    ln+=" "
            ln += f'{words[e-1]}'
            while len(ln) < maxWidth:
                ln += (maxWidth - len(ln)) * " "
            ans.append(ln)
            s = e
        return ans