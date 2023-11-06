class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        return self.recurse(coins, amount)

    def recurse(self, coins, remaining):
        if remaining < 0:
            return -1
        if remaining == 0:
            return 0
        
        if remaining in self.memo:
            return self.memo[remaining]
        
        minCount = -1 
        for coin in coins:
            count = self.recurse(coins, remaining - coin)
            if count != -1:
                minCount = count + 1 if minCount == -1 else min(minCount, count + 1)
        
        self.memo[remaining] = minCount
        
        return self.memo[remaining]
                