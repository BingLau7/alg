#coding:utf-8
"""
    算导16.1-4:
    使用贪心算法求一组活动使用最少的教师完成所有活动
"""
def compatible(start, finish, i):
    """
        求与i兼容最大的活动且值最大
    """
    tmp = []
    len_finish = len(finish)
    for j in range(0, len_finish):
        if start[i] >= finish[j]:
            tmp.append(j)

    return max(tmp)

def greedy_activity_selector(start, finish, i):
    """
        非递归实现
    """
    length = len(start)

    set_k = [i]

    k = i
    for j in range(i+1, length):
        if start[j] >= finish[k]:
            set_k.append(j)
            k = j

    return set_k

def optimal(optimals, start, finish, value):
    """
        答案
    """
    compatibles = [0] * 12
    for i in range(1, 12):
        compatibles[i] = compatible(start, finish, i)

    for i in range(1, 12):
        optimals[i] = max(value[i] + optimals[compatibles[i]], optimals[i-1])


def main():
    """
        Main function
    """
    start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    value = [0, 2, 4, 5, 1, 9, 4, 10, 2, 3, 5, 8]

    optimals = [0] * 12

    optimal(optimals, start, finish, value)
    print optimals

if __name__ == '__main__':
    main()
