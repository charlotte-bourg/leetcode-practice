class Solution:
    from collections import deque
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # shortest path -> BFS
        wordList = set(wordList) # O(n) where n is len wordList

        ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        words = deque([(beginWord, 1)])
        seenWords = {beginWord}

        while words:
            currWord, steps = words.popleft()
            
            if currWord == endWord:
                return steps

            for char in ALPHA:
                for i in range(len(currWord)):
                    neighbor = currWord[:i] + char + currWord[i+1:]
                    if neighbor not in seenWords and neighbor in wordList:
                        words.append([neighbor, steps + 1])
                        print(f"neighbor added is: {neighbor} in {steps+1}")
                        seenWords.add(neighbor)
            
        return 0 

        