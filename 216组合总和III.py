r"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
"""

r'''
分治递归
就这执行用时可以排前1.09%?!
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        init_candidates = list(range(1, 10))

        def recurse(candidates, target, count):
            # print(candidates, target, count)

            if len(candidates) < count:
                return []

            p_max = sum(candidates[-count:])
            p_min = sum(candidates[:count])
            if target > p_max or n < p_min:
                return []
            if target == p_max:
                return [candidates[-count:]]
            if target == p_min:
                return [candidates[:count]]

            if count <= 0:
                return []
            if count == 1:
                if target in candidates:
                    return [[target]]
                else:
                    return []
            if count == 2:
                if len(candidates) == 2:
                    if sum(candidates) == target:
                        return [candidates]
                    else:
                        return []
                lcur = 0
                rcur = len(candidates) - 1
                solutions = []
                while True:
                    if lcur >= rcur:
                        break
                    val = candidates[lcur] + candidates[rcur]
                    if val > target:
                        rcur -= 1
                        continue
                    if val < target:
                        lcur += 1
                        continue
                    solutions.append([candidates[lcur], candidates[rcur]])
                    lcur += 1
                    rcur -= 1
                return solutions
            if count >= 3:
                if len(candidates) == 3:
                    if sum(candidates) == target:
                        return [candidates]
                    else:
                        return []
                new_solutions = []
                for candidate in candidates:
                    new_candidate = [_ for _ in candidates if _ > candidate]
                    solutions = recurse(
                        new_candidate, target=target - candidate, count=count - 1
                    )
                    # print(
                    #     f"solutions:{solutions},new_candidate={new_candidate},target={target-candidate},count={count-1}"
                    # )
                    if len(solutions) > 0:
                        for sol in solutions:
                            new_solutions.append([candidate] + sol)
                return new_solutions

        return recurse(init_candidates, n, k)


k = 4
n = 1
x = Solution()
print(x.combinationSum3(k, n))
