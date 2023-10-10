r'''给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

r'''
直接数连续1分组
'''

class Solution:
    def longestSubarray(self, nums) -> int:
        counts = [[0]]
        temp_zero_flag = False
        is_all_one_flag = True
        for num in nums:
            if num == 0:
                is_all_one_flag = False
                if not temp_zero_flag:
                    if counts[-1][-1] != 0:
                        counts[-1].append(0)
                    temp_zero_flag = True
                else:
                    if not(len(counts[-1]) == 1 and counts[-1][-1] == 0):
                        counts.append([0])
            elif num == 1:
                temp_zero_flag = False
                counts[-1][-1]+=1
        # print(counts)
        if is_all_one_flag:
            return len(nums)-1

        current_solution = 0
        for group in counts:
            if len(group) == 1:
                if group[0] > current_solution:
                    current_solution = group[0]
            else:
                for lcur in range(0,len(group)-1):
                    val = group[lcur]+group[lcur+1]
                    if val > current_solution:
                        current_solution = val

        return current_solution

nums = [1,1,0,1]
# nums = [0,1,1,1,0,1,1,0,1]
# nums = [1,1,1]
# nums = [0,0,0,0,1,1,1,1,0,1,1,0,0,1]
x = Solution()
print(x.longestSubarray(nums))