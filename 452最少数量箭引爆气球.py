r"""有一些球形气球贴在一堵用 XY 平面表示的墙面上。
墙面上的气球记录在整数数组 points ，
其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。
你不知道气球的确切 y 坐标。
一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。
在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，
则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。
弓箭一旦被射出之后，可以无限地前进。
给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
r'''
贪心，按右边界递增排序，
每次选择第一个区间的右边界，则直到有左边界大于所选值的区间
再选择它的右边界
不用纠结哪些被破坏了，因为那后面的气球会被后面的箭顺便破坏
'''

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ret = 1
        x = points[0][1]
        for a,b in points:
            if a > x:
                x = b
                ret +=1
        return ret

points = [[1,2],[2,3],[3,4],[4,5]]
print(Solution().findMinArrowShots(points))
