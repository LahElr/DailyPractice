r"""
给定一个整数数组 asteroids，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，
正负表示行星的移动方向（正表示向右移动，负表示向左移动）。
每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。
碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
如果两颗行星大小相同，则两颗行星都会爆炸。
两颗移动方向相同的行星，永远不会发生碰撞。
"""

r"""
最终状态肯定全部同号，或负数串接正数串
题目保证至少有两个数据，值不会为0
左正右负相撞
从前两个开始，
皆正，负正，负负，各加1
正负，消失的方 向左/右移动

"""

r'''例：
asteroids = [65, 24, 42, 86, 7, 71, -4, 17, 5, -10, -13, 22, -71, 93, -95]
asteroids = [65, 24, 42, 86, 7, 71,     17,    -10, -13, 22, -71, 93, -95]
asteroids = [65, 24, 42, 86, 7, 71,     17,         -13, 22, -71, 93, -95]
asteroids = [65, 24, 42, 86, 7, 71,     17,              22, -71, 93, -95]
asteroids = [65, 24, 42, 86, 7, 71,     17,                  -71, 93, -95]
asteroids = [65, 24, 42, 86, 7, 71,                          -71, 93, -95]
asteroids = [65, 24, 42, 86, 7,                                   93, -95]
asteroids = [65, 24, 42, 86, 7,                                       -95]
asteroids = [-95]

asteroids = [-48, -31, 35, 11, -35, 77, 24, -50, -13, -1, 67, 99, 59, 39]
asteroids = [-48, -31, 35,     -35, 77, 24, -50, -13, -1, 67, 99, 59, 39]
asteroids = [-48, -31,              77, 24, -50, -13, -1, 67, 99, 59, 39]
asteroids = [-48, -31,              77,     -50, -13, -1, 67, 99, 59, 39]
asteroids = [-48, -31,              77,          -13, -1, 67, 99, 59, 39]
asteroids = [-48, -31,              77,               -1, 67, 99, 59, 39]
asteroids = [-48, -31,              77,                   67, 99, 59, 39]

[8, -8, 1]
[       1]

[8,-7,1]
[8,   1]

[6,-7,1]
[  -7,1]
'''

asteroids = [10,2,-5]

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        #lahelr 实现细节：这里用pop在原地执行，省内存，
        #lahelr 但费时，因为python的列表是数组实现，引入了额外的复杂度
        #lahelr 理论上应该是用双向链表最高效
        if len(asteroids)<=1:
            return asteroids
        lcur = 0
        rcur = 1
        while True:
            if rcur>=len(asteroids):
                break
            lval = asteroids[lcur]
            rval = asteroids[rcur]
            if lval>0 and rval<0:
                if lval < -rval:
                    # left gone
                    asteroids.pop(lcur)
                    if lcur>=1:
                        lcur-=1
                        rcur-=1
                    continue
                elif lval > -rval:
                    # right gone
                    asteroids.pop(rcur)
                    continue
                else:
                    # both gone
                    asteroids.pop(lcur)
                    asteroids.pop(lcur)
                    if lcur>=1:
                        lcur-=1
                        rcur-=1
                    continue
            else:
                lcur+=1
                rcur+=1
                continue
        return asteroids

x = Solution()
print(x.asteroidCollision(asteroids))