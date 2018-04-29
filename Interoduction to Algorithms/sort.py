#coding:utf-8
"""
    排序和顺序统计量算法模块
"""
from random import randint


def partition(nums, sub_p, super_r):
    """
        对nums[p..r]原址重排
    """
    pivot = nums[super_r]
    i = sub_p - 1
    for j in range(sub_p, super_r):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[super_r] = nums[super_r], nums[i+1]
    return i+1


def randomized_partition(nums, sub_p, super_r):
    """
        对nums重排
    """
    i = randint(sub_p, super_r)
    nums[super_r], nums[i] = nums[i], nums[super_r]
    return partition(nums, sub_p, super_r)


def randomized_select(nums, sub_p, super_r, i):
    """
        期望为线性时间的选择算法，以快排为原型
        返回nums[p..r]中第i小的元素
    """
    if sub_p == super_r:
        return nums[sub_p]
    index_partition = randomized_partition(nums, sub_p, super_r)     #将数组划分为两个子数组
    k = index_partition - sub_p + 1
    if i == k:
        return nums[index_partition]
    elif i < k:
        return randomized_select(nums, sub_p, index_partition-1, i)
    else:
        return randomized_select(nums, index_partition+1, super_r, i-k)

def test():
    """
        测试函数
    """
    nums = [3, 4, 43, 4, 6, 7, 11, 23]
    print randomized_select(nums, 0, 7, 4)

if __name__ == '__main__':
    test()
