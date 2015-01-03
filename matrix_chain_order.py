#coding:utf-8
"""
    算法导论15-2：矩阵链乘法
"""
from __future__ import print_function

INFINTY = float('inf')

def matrix_chain_order(price):
    """
        自底向上实现
        现在数组0位置全部空闲中,将依照书中数组其实为1的假设改过来
        args:
            price:计算代价
        return:
            recode:记录最短计算代价数组
            process:指出process[i][j]矩阵相乘中i,j中最佳的分割点k
    """
    recode_len = len(price)
    recode = [[None for i in range(recode_len)] for i in range(recode_len)]
    recode = [[None]*recode_len for i in range(recode_len)]
    process = [[None]*recode_len for i in range(recode_len)]
    for i in range(1, recode_len):
        recode[i][i] = 0
    for len_chain in range(2, recode_len):
        for i in range(1, recode_len - len_chain + 1):
            j = i + len_chain - 1
            recode[i][j] = INFINTY
            for k in range(i, j):
                # print 'debug:', i, k, ' ', recode[i][k]
                result = recode[i][k] + recode[k+1][j] + price[i-1] * price[k] * price[j]
                if result < recode[i][j]:
                    recode[i][j] = result
                    process[i][j] = k
    return recode, process


def print_optimal_parens(process, super_script, sub_script):
    """
        输出最优方案过程
        args:
            process:记录分割点k
            super_script:需要计算的上标
            sub_script:需要计算的下标
    """
    if super_script == sub_script:
        print('A'+str(super_script), sep='', end='')
    else:
        print('(', sep='', end='')
        print_optimal_parens(process, super_script, process[super_script][sub_script])
        print_optimal_parens(process, process[super_script][sub_script]+1, sub_script)
        print(')', sep='', end='')

def matrix_multiply(left_matrix, right_matrix):
    """
        计算两矩阵乘积
        return:
            返回left_matrix,right_matrix相乘结果
    """
    if not left_matrix:     #只有一个矩阵的情况下返回right_matrix
        return right_matrix
    left_columns = len(left_matrix[0])
    right_columns = len(right_matrix[0])
    left_row = len(left_matrix)
    right_row = len(right_matrix)
    if left_columns != right_row:
        exit()
    else:
        result_matrix = [[None]*right_columns for i in range(left_row)]
        for i in range(left_row):
            for j in range(right_columns):
                result_matrix[i][j] = 0
                for k in range(left_columns):
                    result_matrix[i][j] =\
                        result_matrix[i][j] + left_matrix[i][k] * right_matrix[k][j]
    return result_matrix

def matrix_chain_multiply(matrixs, process, super_script, sub_script):
    """
        习题15.2——实现矩阵链最优代价乘法计算的真正计算过程
        args:
            matrixs:矩阵序列
            process:matrix_chain_order得到的最优过程表
            super_script:上标
            sub_script:下标
    """
    if super_script == sub_script:
        return matrixs[super_script-1]
    else:
        left_matrix = matrix_chain_multiply(
            matrixs, process,
            super_script, process[super_script][sub_script])
        right_matrix = matrix_chain_multiply(
            matrixs, process,
            process[super_script][sub_script]+1, sub_script)
        result_matrix = matrix_multiply(left_matrix, right_matrix)
        return result_matrix

def recursive_matrix_chain(price, i, j, recode):
    """
        自顶向下
        计算矩阵链乘Ai..j所需要最少标量乘法运算次数m[i,j]，而计算过程是低效的
        args:
            price:代价
            i:第一个乘积矩阵
            j:最后一个乘积矩阵
            recode: 记录二维list，初始为0
        return:
            最小代价
    """
    i, j = i-1, j-1     #强行把i,j变为适应数组，且下面price中的值相应+1
    if i == j:
        return 0
    recode[i][j] = INFINTY
    for k in range(i, j):
        result = recursive_matrix_chain(price, i, k, recode)\
        + recursive_matrix_chain(price, k+1, j, recode)\
        + price[i] * price[k+1] * price[j+1]
        if result < recode[i][j]:
            recode[i][j] = result
    return recode[i][j]

def memoized_matrix_chain(price):
    """
        自顶向下
    """
    recode_len = len(price)-1
    recode = [[None] * (recode_len) for i in range(recode_len)]
    for i in range(recode_len):
        for j in range(recode_len):
            recode[i][j] = INFINTY
    return lookup_chain(recode, price, 0, recode_len-1)

def lookup_chain(recode, price, i, j):
    """
        自顶向下
    """
    if recode[i][j] < INFINTY:
        return recode[i][j]
    if i == j:
        recode[i][j] = 0
    else:
        for k in range(i, j):
            result = lookup_chain(recode, price, i, k)\
            + lookup_chain(recode, price, k+1, j) + price[i-1] * price[k] * price[j]
            if result < recode[i][j]:
                recode[i][j] = result
    return recode[i][j]

def main():
    """
        主函数
    """
    matrix_one = [[1, 1], [2, 0]]
    matrix_two = [[0, 2, 3], [1, 1, 2]]
    matrix_three = [[2, 1], [3, 2], [4, 1]]
    price = [2, 2, 3, 2]
    # recode = [[None for i in range(5)] for i in range(5)]
    # print(recursive_matrix_chain(price, 1, 3, recode))
    print(memoized_matrix_chain(price))
    # recode, process = matrix_chain_order(price)
    # print(recode[1][3])
    # print_optimal_parens(process, 1, 3)
    # print()
    # result_matrix = matrix_chain_multiply([matrix_one, matrix_two, matrix_three], process, 1, 3)
    # print(result_matrix)

if __name__ == '__main__':
    main()
