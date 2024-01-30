from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 2:
            return []
        elif n == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums.sort()
        ret = []
        # -4, -1, -1, 0, 1, 2
        for cur in range(0, n - 2):
            d = nums[cur]
            if cur > 0 and d == nums[cur - 1]:
                continue
            left_ptr = cur + 1
            right_ptr = n - 1

            while right_ptr > left_ptr:
                right = nums[right_ptr]
                left = nums[left_ptr]
                if left_ptr >= cur + 2 and left == nums[left_ptr - 1]:
                    left_ptr += 1
                    continue
                if right_ptr <= n - 2 and right == nums[right_ptr + 1]:
                    right_ptr -= 1
                    continue
                s = right + left + d
                if s == 0:
                    ret.append([d, left, right])
                    left_ptr += 1
                    right_ptr -= 1
                elif s < 0:
                    left_ptr += 1
                    continue
                elif s > 0:
                    right_ptr -= 1
                    continue
        return ret


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
