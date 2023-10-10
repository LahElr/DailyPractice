r'''给定一个区间的集合 intervals ，
其中 intervals[i] = [starti, endi] 。
返回 需要移除区间的最小数量，使剩余区间互不重叠 。
'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        lcur = 0
        rcur = 1
        l = len(intervals)
        ans = 0
        while True:
            if rcur >= l:
                break
            if intervals[rcur][0]<intervals[lcur][1]:
                ans+=1
                rcur+=1
                continue
            else:
                lcur = rcur
                rcur+=1
                continue
        return ans

# intervals = [[1,2],[1,3],[2,3],[3,4]]
# intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
print(Solution().eraseOverlapIntervals(intervals))