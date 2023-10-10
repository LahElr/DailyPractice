r'''给定一个长度为 n 的整数数组 height 。
有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
'''

#lahelr 双指针

# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

# max(min(h[i_1],h[i_2])*(i_2-i_1))
# sol[x,y] = 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lcur = 0
        rcur = len(height)-1
        sol_cand = 0
        while True:
            if lcur >= rcur:
                return sol_cand
            lheight = height[lcur]
            rheight = height[rcur]
            if lheight<=rheight:
                sq = (rcur-lcur)* lheight
                if sq>sol_cand:
                    sol_cand = sq
                lcur+=1
                continue
            else:
                sq = (rcur-lcur)* rheight
                if sq>sol_cand:
                    sol_cand = sq
                rcur-=1
                continue

            

x = Solution()
print(x.maxArea(height))