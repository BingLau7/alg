#!/usr/bin/env python
# encoding: utf-8

"""
    快速排序
"""
import random
import sys

compared_number = 0

def quick_sort(arr, left, right):
    """
        快速排序 """
    if left < right:
        tmp = meddle_of_three_partition(arr, left, right)
        # tmp = other_partition(arr, left, right)
        quick_sort(arr, left, tmp-1)
        quick_sort(arr, tmp+1, right)

def other_partition(arr, left, right):
    """
        coursera中的实现
    """
    # arr[left], arr[right] = arr[right], arr[left]
    pivot = arr[left]
    i = left + 1
    j = left + 1
    global compared_number
    while j <= right:
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    arr[left], arr[i-1] = arr[i-1], arr[left]
    compared_number += right - left
    return i-1

def partition(arr, left, right):
    """
        得到主元并原址重排
    """
    # arr[left], arr[right] = arr[right], arr[left]
    pivot = arr[right]
    i = left - 1
    j = left
    global compared_number
    while j <= right - 1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
        # compared_number += 1
    arr[i+1], arr[right] = arr[right], arr[i+1]
    compared_number += right - left
    return i+1

def randomized_partition(arr, left, right):
    """
        随机选择主元
    """
    i = random.randint(left, right)
    arr[right], arr[i] = arr[i], arr[right]
    return partition(arr, left, right)

def meddle_of_three_partition(arr, left, right):
    """
        三分选择主元
    """
    middle_index = left + (right - left) / 2
    pivot_index = arr.index(sorted([arr[left], arr[middle_index], arr[right]])[1])
    # arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    if pivot_index != left:
        arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    # return partition(arr, left, right)
    return other_partition(arr, left, right)

def main():
    """
        测试函数
    """
    arr = [34, 2, 31, 1, 7, 43, 21, 90, 19]

    # while True:
    #     line = sys.stdin.readline()
    #     if not line:
    #         break
    #     arr.append(int(line))

    quick_sort(arr, 0, len(arr)-1)
    print arr
    # print compared_number

if __name__ == '__main__':
    main()
