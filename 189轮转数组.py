from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n <= 1:
            return

        k = k % n  # the input is guaranteed not to be an empty array
        if k == 0:
            return

        t = nums[0]
        ct = 0
        cur_start = 0
        tgt = 0
        next_tgt = k
        start_flag = False
        while ct < n:
            if tgt == cur_start and start_flag:
                cur_start += 1
                tgt = cur_start
                t = nums[cur_start]
                start_flag = False
                continue
            next_tgt = (tgt + k) % n
            nums[next_tgt], t = t, nums[next_tgt]
            ct += 1
            tgt = next_tgt
            start_flag = True
            print(nums)
        return


nums = [-1, -100, 3, 99]
Solution().rotate(nums, 2)
print(nums)
