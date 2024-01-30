from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        prev_peak_pos = prev_low_pos = -1
        prev_peak_own = 0
        ret = 0

        for i, rating in enumerate(ratings):
            if i == 0 or ratings[i - 1] == rating:
                ret += 1
                prev_peak_pos = prev_low_pos = i
                prev_peak_own = 1
            elif ratings[i - 1] > rating:
                prev_low_pos = i
                ret += 1 + i - prev_peak_pos - 1
                if 1 + i - prev_peak_pos > prev_peak_own:
                    ret += 1
            elif ratings[i - 1] < rating:
                prev_peak_pos = i
                ret += 1 + i - prev_low_pos
                prev_peak_own = 1 + i - prev_low_pos

        return ret
