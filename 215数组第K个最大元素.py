from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num for num in nums[:k]]
        heapq.heapify(heap) #! inplace!
        for i in range(k,len(nums)):
            num = nums[i]
            current_kth_top = heap[0]
            if num>current_kth_top:
                heapq.heapreplace(heap,num)
        return heap[0]
    
data = [1,2,2,3,3,4,5,5,6]
k = 4
print(Solution().findKthLargest(data,k))
