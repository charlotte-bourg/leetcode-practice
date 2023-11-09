class Solution:
    from collections import deque
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # shortest path -> BFS
        wordList = set(wordList) # O(n) where n is len wordList

        l = len(beginWord) # words are the same length 
        ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        words = deque([(beginWord, 1)])
        seenWords = {beginWord}

        while words:
            currWord, steps = words.popleft()
            
            if currWord == endWord:
                return steps

            for char in ALPHA: # O(1)
                for i in range(l): # O(m) where m is len words
                    neighbor = currWord[:i] + char + currWord[i+1:]
                    if neighbor not in seenWords and neighbor in wordList:
                        words.append([neighbor, steps + 1])
                        seenWords.add(neighbor)
            
        return 0 

        