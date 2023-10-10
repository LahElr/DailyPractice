r'''
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

r'''
__  _____  ____  
\ \/ / _ \|  _ \ 
 \  / | | | |_) |
 /  \ |_| |  _ < 
/_/\_\___/|_| \_\
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res^num
        return res

nums = [2,2,1]
print(Solution().singleNumber(nums))
