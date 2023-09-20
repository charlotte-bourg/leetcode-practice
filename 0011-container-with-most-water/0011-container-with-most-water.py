class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0 
        i = 0 
        j = len(height) - 1
        while j > i: 
            volume = max(volume, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1 
            else: 
                j -= 1 
        return volume

        