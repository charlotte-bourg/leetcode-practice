class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insStart = 10 ** 5 + 1
        insEnd = -1
        insLoc = 0
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]: # if newInterval ends before 1st existing interval starts
            intervals.insert(0, newInterval)
            return intervals 
        if newInterval[0] > intervals[len(intervals) - 1][1]: # if newIntervals starts after last existing interval ends
            intervals.append(newInterval)
            return intervals 
        i = 0 
        while i < len(intervals):
            if i <= len(intervals) - 1:
                print(f"{newInterval[0]} {intervals[i][1]}")
                if newInterval[0] > intervals[i][1] and newInterval[1] < intervals[i+1][0]:
                    intervals.insert(i+1, newInterval)
                    return intervals
            if (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][0]) or (newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][1]): 
                if not insLoc:
                    insLoc = i
                insEnd = max([newInterval[1], intervals[i][1], insEnd])
                insStart = min([newInterval[0], intervals[i][0], insStart])
                del intervals[i]
            else:
                i += 1  
        if insStart != 10 ** 5 + 1:
            intervals.insert(insLoc, [insStart, insEnd])
        return intervals 