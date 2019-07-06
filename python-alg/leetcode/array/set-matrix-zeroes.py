from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])
        # 记录第一行第一列是否存在需要变化的可能
        y = False
        for i in range(n):
            if matrix[i][0] == 0:
                y = True
        x = False
        for j in range(m):
            if matrix[0][j] == 0:
                x = True
        # 处理刨除第一行第一列的值
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(n):
            for j in range(m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if y:
            for i in range(n):
                matrix[i][0] = 0
        if x:
            for j in range(m):
                matrix[0][j] = 0


if __name__ == '__main__':
    # _input = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 1]
    # ]
    # _input = [
    #     [0, 1, 2, 0],
    #     [3, 4, 5, 2],
    #     [1, 3, 1, 5]
    # ]
    _input = [[1, 1, 1], [0, 1, 2]]
    Solution().setZeroes(_input)
    print(_input)
