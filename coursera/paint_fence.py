#coding:utf-8
"""
给定一组长度为 n 的栅栏，从左到右高度依次是 h[i]。
你需要对这个栅栏粉刷油漆，每次你可以粉刷一行或者一列。
问最少粉刷几次，可以给所有栅栏上漆。（不能多刷）

输入格式:
    第一行包含一个整数，表示栅栏的长度。
    接下来的一行，包含 n 个数（n <= 100000），依次表示 h[i](h[i] <= 10^9)。

    输出格式：
    输出一行表示对应的答案。

    输入样例：
    5
    2 2 1 2 1

    输出样例：
    3

思路：每次都找局部最小的
"""
def get_min(left, right, arr):
    """
        getMinForPaintFence
    """
    num_min = float('inf')
    for i in range(left, right):
        num_min = min(num_min, arr[i])

    times = num_min
    print 'time:', times
    right_next = 0
    for i in range(left, right):
        if arr[i] == num_min:
            continue
        right_next = i+1
        while right_next and arr[right_next] != num_min:
            right_next += 1
        right_next -= 1
        for j in range(i, right_next):
            arr[j] -= num_min
        times += get_min(i, right_next, arr)
    return min(right-left+1, times)

def main():
    """
        Main Function
    """
    num = int(raw_input())
    nums = raw_input()
    arr_input = [int(x) for x in nums.split(' ')]

    times = get_min(0, num-1, arr_input)
    print times

if __name__ == '__main__':
    main()
