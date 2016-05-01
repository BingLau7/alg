#coding:utf-8
"""
    双调欧几里得旅行商问题：

    欧几里得旅行商问题：给定平面上n个点作为输入，希望求出连接所有n个点的最短巡游路径

    双调巡游：即从最左边开始，严格向右前进，直至最右边的点，
    然后调头严格向左前进，直至回到起始点
"""
import math

def cal_distance(coordinate_x, coordinate_y):
    """
        计算坐标间距离
    """
    tmp_x = (coordinate_x[0] - coordinate_y[0])**2
    tmp_y = (coordinate_x[1] - coordinate_y[1])**2
    return math.sqrt(tmp_x+tmp_y)

def length(coordinates):
    """
        计算最佳长度
    """
    print coordinates

def main():
    """
        Main function
    """
    coordinates = [(0, 0), (1, 6), (2, 3), (5, 2), (6, 5), (8, 1), (9, 4)]
    length(coordinates)

if __name__ == '__main__':
    main()
