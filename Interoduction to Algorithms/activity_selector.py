# coding:utf-8

"""
    活动选择问题
"""


def recursive_activity_selector(start, finish, set_k, scale):
    """
        迭代实现
    """
    i = set_k + 1
    while i <= scale and start[i] < finish[set_k]:
        i += 1

    print i, scale
    if i <= scale:
        tmp = recursive_activity_selector(start, finish, i, scale)
        tmp.append(i)
        return tmp
    else:
        return []


def greedy_activity_selector(start, finish):
    """
        非递归实现
    """
    length = len(start)

    set_k = [1]

    k = 1
    for i in range(2, length):
        if start[i] >= finish[k]:
            set_k.append(i)
            k = i

    return set_k


def main():
    """
        Main function
    """
    start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    # print recursive_activity_selector(start, finish, 0, 11)
    print greedy_activity_selector(start, finish)

if __name__ == '__main__':
    main()
