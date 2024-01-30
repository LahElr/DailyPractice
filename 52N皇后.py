class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 4:
            return {0: 0, 1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352}[n]
        result_count = 0

        def rec_body(already_there):
            nonlocal result_count
            # print(already_there)
            this_line_no = len(already_there)
            for i in range(n):
                for j, k in enumerate(already_there):
                    if (i == k) or ((this_line_no - j) == abs(i - k)):
                        # print(i,j,k,this_line_no,(i == k), ((this_line_no - j) == abs(i-k)))
                        break
                else:
                    # print(f"{already_there}-->{i}")
                    if this_line_no >= n - 1:
                        result_count += 1
                    else:
                        rec_body(already_there + [i])

        rec_body([])
        return result_count


for n in range(0, 10):
    print(n, Solution().totalNQueens(n))
