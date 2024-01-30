from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_bound = 0
        right_bound = len(matrix[0]) - 1
        up_bound = 1
        down_bound = len(matrix) - 1

        direction = 0
        x = 0
        y = 0
        ret = []
        output_flag = True
        direction_flag = False

        while True:
            if output_flag:
                ret.append(matrix[x][y])
            else:
                output_flag = True

            if direction == 0:
                if y >= right_bound:
                    direction = 1
                    right_bound -= 1
                    output_flag = False
                    if direction_flag:
                        return ret
                    else:
                        direction_flag = True
                else:
                    y += 1
                    if direction_flag:
                        direction_flag = False
            elif direction == 1:
                if x >= down_bound:
                    direction = 2
                    down_bound -= 1
                    output_flag = False
                    if direction_flag:
                        return ret
                    else:
                        direction_flag = True
                else:
                    x += 1
                    if direction_flag:
                        direction_flag = False
            elif direction == 2:
                if y <= left_bound:
                    direction = 3
                    left_bound += 1
                    output_flag = False
                    if direction_flag:
                        return ret
                    else:
                        direction_flag = True
                else:
                    y -= 1
                    if direction_flag:
                        direction_flag = False
            elif direction == 3:
                if x <= up_bound:
                    direction = 0
                    up_bound += 1
                    output_flag = False
                    if direction_flag:
                        return ret
                    else:
                        direction_flag = True
                else:
                    x -= 1
                    if direction_flag:
                        direction_flag = False
