# coding:utf-8
"""
    算导15-4:最长公共子序列
"""
UP = 'U'
LEFT = 'L'
DIAGONAL = 'D'


def lcs_length(sequence_x, sequence_y):
    """
        计算x，y的最长子序列长度length
    """
    length_x = len(sequence_x)
    length_y = len(sequence_y)

    recode = [[None] * length_y for i in range(length_x)]
    length = [[None] * (length_y + 1) for i in range(length_x + 1)]

    for i in range(length_x):
        length[i + 1][0] = 0
    for j in range(length_y):
        length[0][j + 1] = 0
    for i in range(length_x):
        for j in range(length_y):
            if sequence_x[i] == sequence_y[j]:
                length[i + 1][j + 1] = length[i][j] + 1
                recode[i][j] = DIAGONAL
            elif length[i][j + 1] >= length[i + 1][j]:
                length[i + 1][j + 1] = length[i][j + 1]
                recode[i][j] = UP
            else:
                length[i + 1][j + 1] = length[i + 1][j]
                recode[i][j] = LEFT
    return length, recode


def print_lcs(recode, sequence_x, i, j):
    """
        打印出LCS
    """
    if i == -1 or j == -1:
        return
    if recode[i][j] == DIAGONAL:
        print_lcs(recode, sequence_x, i - 1, j - 1)
        print sequence_x[i]
    elif recode[i][j] == UP:
        print_lcs(recode, sequence_x, i - 1, j)
    else:
        print_lcs(recode, sequence_x, i, j - 1)


def main():
    """
        Main function
    """
    sequence_x = list('ABCBDAB')
    sequence_y = list('BDCABA')

    length, recode = lcs_length(sequence_x, sequence_y)
    print_lcs(recode, sequence_x, 6, 5)


if __name__ == '__main__':
    main()
