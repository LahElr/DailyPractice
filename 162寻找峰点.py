from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums)-1
        cur = 0
        while True:
            if left == right-1:
                if nums[left]> nums[right]:
                    return left
                else:
                    return right
            #if left >= right:
            #    raise ValueError
            cur = (left+right)//2
            a = nums[cur-1] if cur >left else -float('inf')
            b = nums[cur]
            c = nums[cur+1] if cur <right else -float('inf')
            if a>b and b>c:
                right = cur
                continue
            if a > b and b<c:
                right = cur
                continue
            if a < b and b>c:
                return cur
            if a < b and b<c:
                left = cur
                continue