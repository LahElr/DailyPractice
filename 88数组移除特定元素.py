class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) <= 0:
            return 0
        elif len(nums) <= 1:
            return 0 if nums[0] == val else 1
        cur_read = 0
        cur_write = 0
        l = len(nums)
        while True:
            if cur_read >= l:
                break
            v = nums[cur_read]
            if v == val:
                cur_read += 1
                continue
            else:
                nums[cur_write] = v
                cur_write += 1
                cur_read += 1
        return cur_write
