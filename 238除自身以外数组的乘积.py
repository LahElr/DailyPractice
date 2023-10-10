r"""给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

r'''
官方题解提出的优化方法：
由于输出数组不算在空间复杂度内，那么我们可以将 L 或 R 数组用输出数组来计算。
先把输出数组当作 L 数组来计算，然后再动态构造 R 数组得到结果。
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1 for _ in range(len(nums))]
        postfix_product = [1 for _ in range(len(nums))]

        prefix_product[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_product[i] = nums[i] * prefix_product[i - 1]

        postfix_product[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix_product[i] = nums[i] * postfix_product[i + 1]

        answer = [
            (prefix_product[i - 1] if i >= 1 else 1)
            * (postfix_product[i + 1] if i < len(nums) - 1 else 1)
            for i in range(len(nums))
        ]
        return answer


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
