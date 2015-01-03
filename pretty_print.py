#coding:utf-8
"""
    算导思考题15-4：整齐打印
"""
MAX = 20
INFINITE = float('inf')

def left_space(length):
    """
        求剩余空格数立方
    """
    num = len(length)
    left_space_cube = [[0]*(num+1) for i in range(num+1)]
    for i in range(1, num+1):
        for j in range(i, num+1):
            words_length = sum(length[i:j+1])
            extra = MAX - j + i - words_length
            if extra < 0:
                left_space_cube[i][j] = INFINITE
            elif j == num and extra > 0:
                left_space_cube[i][j] = 0
            else:
                left_space_cube[i][j] = extra **3

    return left_space_cube




def pretty_print(length):
    """
        整齐打印函数
        record[i]=min1≤k<i(record(k)+left_space(k+1,i))
    """
    num = len(length)

    record = [0]*(num+1)    #存放问题的解
    solution_k = [0]*(num+1)    #存放最优解k

    left_space_cube = left_space(length)
    for j in range(1, num+1):
        record[j] = record[0] + left_space_cube[1][j]
        solution_k[j] = 1
        for k in range(1, j):
            tmp = record[k-1] + left_space_cube[k][j]
            record[j] = min(record[j], tmp)

    return record, solution_k


def main():
    """
        Main function
    """
    length = [10, 6, 7, 2, 4, 8, 5, 6, 3]
    print pretty_print(length)

if __name__ == '__main__':
    main()
