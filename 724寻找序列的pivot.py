r'''
返回“左侧所有元素和==右侧所有元素和”的数的下标
'''

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left_sum = 0
        right_sum = sum(nums[1:])
        if left_sum == right_sum:
            return 0
        for i, num in enumerate(nums[1:]):
            left_sum += nums[i]
            right_sum -= nums[i+1]
            if left_sum == right_sum:
                return i+1
        return -1