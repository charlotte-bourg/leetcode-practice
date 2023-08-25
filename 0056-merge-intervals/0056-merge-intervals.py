class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(intervals) == 0:
            return ans
        intervals.sort() #sort so that the starting value is increasing through list
        s = intervals[0][0] 
        e = intervals[0][1]
        i = 1 
        while i < len(intervals):
            if intervals[i][0] >= s and intervals[i][0] <= e:
                e = max(intervals[i][1],e)
            else:
                ans.append([s,e])
                s = intervals[i][0]
                e = intervals[i][1]
            i += 1
        ans.append([s,e])
        return ans 


