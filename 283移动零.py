r"""给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lcur = 0
        rcur = 0
        l = len(nums)
        if l <= 1:
            return
        while rcur < l:
            if nums[rcur] != 0:
                nums[lcur], nums[rcur] = nums[rcur], nums[lcur]
                rcur += 1
                lcur += 1
            else:
                rcur += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
