r'''我懒得复制问题了
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/dota2-senate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#lahelr 双队列来模拟这一互相禁言的过程
#lahelr 这个deque效率好高啊

import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_d = collections.deque()
        queue_r = collections.deque()
        n = len(senate)
        for i,ch in enumerate(senate):
            if ch=='R':
                queue_r.append(i)
            else:
                queue_d.append(i)
        while True:
            if len(queue_d) == 0:
                return "Radiant"
            if len(queue_r) == 0:
                return "Dire"
            d = queue_d.popleft()
            r = queue_r.popleft()
            if d < r:
                queue_d.append(d+n)
            else:
                queue_r.append(r+n)
        


senate = "DDRRR" # 不能简单比数量的反例
print(Solution().predictPartyVictory(senate))