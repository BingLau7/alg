from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 转置矩阵
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        Solution.print_image(matrix)
        # 左右对称转换
        max_index = len(matrix) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][max_index-j] = matrix[i][max_index-j], matrix[i][j]
        Solution.print_image(matrix)

    @staticmethod
    def print_image(matrix: List[List[int]]):
        for l in matrix:
            print(l)


if __name__ == '__main__':
    _input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(_input)
