r'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

*最开始想的是排序，然后二分搜到0，去一个个匹配，时间复杂度是O(NlogN+logN+N)，但是空间复杂度的确是常数
实际上是从哈希表遍历的思路优化，分多次遍历，将输入空间用作哈希表
'''

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num <=0 or num>=n:
                nums[i] = n+1
        for num in nums:
            if 0<num<n:
                nums[num-1] = - nums[num-1]
        for i, num in enumerate(nums):
            if num>=0:
                return i+1
        return n
            