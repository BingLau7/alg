#coding:utf-8
"""
    算导15-5：最优二叉搜索树
"""
INFINITY = float('inf')
def optimal_bst(probability_k, probability_d, scale):
    """
        计算最优二叉搜索树的期望搜索代价
        返回：
            expect:expect[i,j]包含关键字ki,...,kj的最优二叉
                搜索树中进行一次搜索的期望代价
            roots:root[i,j]记录包含关键字ki,...,kj的子树的根。
    """
    expect = [[0.0]*(scale+1) for i in range(scale+2)]
    total_probability = [[0.0]*(scale+1) for i in range(scale+2)]
    roots = [[None]*(scale+1) for i in range(scale+1)]

    for i in range(1, scale+2):
        expect[i][i-1] = probability_d[i-1]
        total_probability[i][i-1] = probability_d[i-1]

    for k in range(1, scale+1):
        for i in range(1, scale-k+2):
            j = i + k - 1
            expect[i][j] = INFINITY
            total_probability[i][j] = total_probability[i][j] + \
                    probability_k[j] + probability_d[j]
            for root in range(i, j+1):
                tmp = expect[i][root-1] + expect[root+1][j] + total_probability[i][j]
                if tmp < expect[i][j]:
                    expect[i][j] = tmp
                    roots[i][j] = root

    return expect, roots

def main():
    """
        Main function
    """
    probability_k = [0.00, 0.15, 0.10, 0.05, 0.10, 0.20]
    probability_d = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    expect, roots = optimal_bst(probability_k, probability_d, 5)
    print roots


if __name__ == '__main__':
    main()
