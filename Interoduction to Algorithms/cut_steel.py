#coding:utf-8
"""
    算法导论切割钢条算法
"""
NEGATIVE_INFINITY = float('-inf')
CUT_COST = 1

def memoized_cut_aux(price, num, record):
    """
        带备忘的自顶向下方法
    """
    if record[num] >= 0:
        return record[num]

    if num == 0:
        result = 0
    else:
        result = float('-inf')
        for i in range(1, num+1):
            result = max(result, price[i] + memoized_cut_aux(price, num-i, record))
    record[num] = result
    return result

def extended_memoized_cut_aux(price, num, record, cut_length):
    """
        带备忘的自顶向下方法
        可以记录最佳方案
    """
    if record[num] >= 0:
        return record[num]

    if num == 0:
        result = 0
    else:
        result = float('-inf')
        for i in range(1, num+1):
            tmp_result = price[i] + extended_memoized_cut_aux(price, num-i, record, cut_length)
            if result < tmp_result:
                cut_length[num] = i
                result = tmp_result
    record[num] = result
    return result

def memoized_cut_rod(price, num, cut_length):
    """
        初始化记忆数组
    """
    record = [NEGATIVE_INFINITY] * (num+1)
    return extended_memoized_cut_aux(price, num, record, cut_length)

def bottom_up_cut_rod(price, num):
    """
        自底向上方法
    """
    record = [[] for i in range(num+1)]
    record[0] = 0
    for j in range(1, num+1):
        result = NEGATIVE_INFINITY
        for i in range(1, j+1):
            result = max(result, price[i] + record[j-i])
        record[j] = result
    return record[num]

def extended_bottom_up_cut_rod(price, num):
    """
        扩展版
    """
    record = [[] for i in range(num+1)]
    cut_length = [[] for i in range(num+1)]
    record[0] = 0
    for j in range(1, num+1):
        result = NEGATIVE_INFINITY
        for i in range(1, j+1):
            if result < price[i] + record[j-i]:
                result = price[i] + record[j-i]
                cut_length[j] = i
        record[j] = result
    return result, cut_length

def cost_bottom_up_cut_rod(price, num):
    """
        15.1-3
        分割还要付出多余的切割成本CUT_COST
    """
    record = [[] for i in range(num+1)]
    cut_length = [[] for i in range(num+1)]
    record[0] = 0
    for j in range(1, num+1):
        result = NEGATIVE_INFINITY
        for i in range(1, j+1):
            if result < price[i] + record[j-i] - CUT_COST:
                result = price[i] + record[j-i] - CUT_COST
                cut_length[j] = i
        record[j] = result
    return result, cut_length


def print_cut_solution(price, num):
    """
        打印切割方案
    """
    cut_length = [None]*(num+1)
    result = memoized_cut_rod(price, num, cut_length)
    while num > 0:
        print cut_length[num]
        num = num - cut_length[num]
    return result

def main():
    """
        Main function
    """
    length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    price_table = dict(zip(length, price))
    print print_cut_solution(price_table, 4)

if __name__ == '__main__':
    main()
