r"""给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，
两者长度都是 n ，再给你一个正整数 k 。
你必须从 nums1 中选一个长度为 k 的 子序列 对应的下标。

对于选择的下标 i0 ，i1 ，...， ik - 1 ，你的 分数 定义如下：
nums1 中下标对应元素求和，乘以 nums2 中下标对应元素的 最小值 。
用公示表示： 
(nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * 
    min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]) 。
请你返回 最大 可能的分数。

一个数组的 子序列 下标是集合 {0, 1, ..., n-1} 中删除若干元素得到的剩余集合，也可以不删除任何元素。
"""

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True)
        heap = [_[0] for _ in nums[:k]]
        heapq.heapify(heap)
        heap_sum = sum(heap)
        ret = heap_sum * nums[k - 1][1]
        # 初始状态，选nums2中最大的k个
        for a, b in nums[k:]:
            # b一定比上一个状态的nums2最小值更小
            if a > heap[0]:
                heap_sum += a - heapq.heapreplace(heap, a)
                ret = max(ret, heap_sum * b)
        return ret


# nums1 = [1,3,3,2]
nums1 = [1000,1,3,2]
# nums1 = [4,2,3,1,1]
# nums1 = [1, 4]

nums2 = [1,2,3,4]
# nums2=[7,5,10,9,6]
# nums2 = [3, 1]
k = 2
print(Solution().maxScore(nums1, nums2, k))
