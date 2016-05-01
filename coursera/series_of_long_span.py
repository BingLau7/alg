#coding:utf-8
"""
 题目内容：
 给定长度为 n 的数列 {an}，记 s(l, r) 为 [l, r] 区间里最大数与最小数的差。
 询问所有 s(l, r) 的的积（数据保证是随机生成的）

 输入格式:
    第一行包含一个整数 n (1 <= n <= 10^5) 表示数列的项数。
    第二行包含 n 个整数 ai (0 <= ai <= 10^9) 表示数列中的每项。

    输出格式：
    一行一个整数表示答案模 10^9 + 7　后的结果。

    输入样例：
    3
    1 2 4

    输出样例：
    6

    备注：这里将题目中的l认为是数字1,情况简单，但原理类似
"""

def get_multiplication_1tor(arr, right):
    """
        得到 a[1-r] 最小数和最大数的差
        递归调用算出结果

        args:
            arr:input arr
            right:r

        return:
            a[1-r]最小数和最大数的差
    """
    tmp_arr = [arr[i] for i in range(right+1)]

    if not tmp_arr:
        return

    max_arr = max(tmp_arr)
    min_arr = min(tmp_arr)
    index_max = tmp_arr.index(max_arr)
    index_min = tmp_arr.index(min_arr)
    result = max_arr - min_arr

    if index_max > index_min:
        if right == index_max:
            right -= 1
        else:
            result **= right - index_max
            right = index_max - 1

    if index_min > index_max:
        if right == index_min:
            right -= 1
        else:
            result **= right - index_min
            right = index_min - 1

    print 'result', result, 'right', right

    if index_min == index_max:
        return


    if not right:
        return result
    else:
        result *= get_multiplication_1tor(tmp_arr, right)

    if not right:
        return

    return result


def main():
    """
        The main function
    """
    num = int(raw_input())
    nums = raw_input()
    arr_input = [int(x) for x in nums.split(' ')]

    result = get_multiplication_1tor(arr_input, num-1)
    print result


if __name__ == '__main__':
    main()

