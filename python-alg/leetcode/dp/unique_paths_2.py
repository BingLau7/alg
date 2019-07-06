from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid[0]), len(obstacleGrid)
        paths_num = [[0 for i in range(n)] for i in range(m)]

        if obstacleGrid[0][0] != 1:
            paths_num[0][0] = 1

        # 初始化表格最左
        for i in range(m):
            if obstacleGrid[i][0] != 1 and i != 0:
                paths_num[i][0] = paths_num[i-1][0]

        # 初始化表格最上
        for j in range(n):
            if obstacleGrid[0][j] != 1 and j != 0:
                paths_num[0][j] = paths_num[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    paths_num[i][j] = paths_num[i-1][j] + paths_num[i][j-1]

        return paths_num[-1][-1]

if __name__ == '__main__':
    m, n = 3, 3
    # arr = [[0 for i in range(n)] for i in range(m)]
    # arr[1][1] = 1
    arr = [[0, 1]]
    print(Solution().uniquePathsWithObstacles(arr))