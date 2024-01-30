import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        d = [] # the smallest number of the ascending series of length `i`
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                k = bisect.bisect_left(d,num)
                d[k] = num
        return len(d)



    def dp_lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=1:
            return n
        solutions = [1 for _ in range(n)]
        ret = 0
        for i in range(n):
            for j in range(i+1):
                if nums[j]<nums[i]:
                    solutions[i] = max(solutions[i],solutions[j]+1)
            ret = max(ret,solutions[i])
        return ret

# x = [0,1,0,3,2,3]
# x = [10,9,2,5,3,7,101,18]
x = [7,7,7,7,7,7,7]
# x = [4,10,4,3,8,9]
print(Solution().lengthOfLIS(x))
print(Solution().dp_lengthOfLIS(x))