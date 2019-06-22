from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, left = 0, -1
        down = len(matrix)
        right = 0
        if down > 0:
            right = len(matrix[0])
            if right == 0:
                return []
        else:
            return []

        # 方向 1, 2, 3, 4 对应 右，下，左, 上
        direction = 1
        def up_fun(i, j): return i - 1, j
        def down_fun(i, j): return i + 1, j
        def right_fun(i, j): return i, j + 1
        def left_fun(i, j): return i, j - 1
        direction_fun_map = {
            1: right_fun,
            2: down_fun,
            3: left_fun,
            4: up_fun
        }

        res = []
        i, j = 0, 0
        total = len(matrix) * len(matrix[0])
        while len(res) != total:
            res.append(matrix[i][j])
            # 判断是否到边界以及是否要设置新的边界及方向
            if i + 1 == down and direction == 2:
                direction = 3
                down -= 1
            elif i - 1 == up and direction == 4:
                direction = 1
                up += 1
            elif j - 1 == left and direction == 3:
                direction = 4
                left += 1
            elif j + 1 == right and direction == 1:
                direction = 2
                right -= 1
            f = direction_fun_map[direction]
            i, j = f(i, j)
        return res


if __name__ == '__main__':
    _input = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(_input))
