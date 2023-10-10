r'''有 n 个房间，房间按从 0 到 n - 1 编号。
最初，除 0 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。
然而，你不能在没有获得钥匙的时候进入锁住的房间。
当你进入一个房间，你可能会在里面找到一套不同的钥匙，
每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。
给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。如果能进入 所有 房间返回 true，否则返回 false。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/keys-and-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

r'''
树遍历
'''

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visiting_stack = [0]
        visitable = [1 if _==0 else 0 for _ in range(len(rooms))]
        while True:
            if len(visiting_stack) == 0:
                break
            room_to_visit = visiting_stack.pop()
            keys_given = rooms[room_to_visit]
            for key in keys_given:
                if visitable[key] == 0:
                    visitable[key] = 1
                    visiting_stack.append(key)
        return sum(visitable) == len(rooms)



rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))