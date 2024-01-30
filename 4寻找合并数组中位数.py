from typing import List


class Solution:
    def __findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        tgt = (m + n - 1) // 2
        dbl_tgt = (m + n) % 2 == 0

        if m == 0:
            if dbl_tgt:
                return (nums2[tgt] + nums2[tgt + 1]) / 2
            else:
                return nums2[tgt]
        if n == 0:
            if dbl_tgt:
                return (nums1[tgt] + nums1[tgt + 1]) / 2
            else:
                return nums1[tgt]

        ptrs = [0, 0]
        nums = [nums1, nums2]
        lens = (m, n)
        ct = 0
        this = 0 if nums1[0] <= nums2[0] else 1
        friend = 1 if this == 0 else 0

        def get_val_friend():
            if ptrs[friend] > lens[friend] - 1:
                return float("inf")
            else:
                return nums[friend][ptrs[friend]]

        def get_val_next():
            if ptrs[this] >= lens[this] - 1:
                return float("inf")
            else:
                return nums[this][ptrs[this] + 1]

        while True:
            if ct == tgt:
                break

            val_next = get_val_next()
            val_friend = get_val_friend()

            ptrs[this] += 1
            if val_next > val_friend:
                this, friend = friend, this
            ct += 1

        if dbl_tgt:
            a = nums[this][ptrs[this]]

            val_next = get_val_next()
            val_friend = get_val_friend()
            b = min(val_next, val_friend)

            return (a + b) / 2
        else:
            return nums[this][ptrs[this]]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            r"""
            作者：力扣官方题解
            链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/258842/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
            来源：力扣（LeetCode）
            著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (
                getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)
            ) / 2
