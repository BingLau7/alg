#coding:utf-8
"""
    最长回文子序列
"""

#record记录常量
UP = 0
LEFT = 1
DIAGONAL = 2

def lps(sequence_x):
    """
        自底向上构件最长回文子序列
        re
    """
    length_x = len(sequence_x)

    length = [[0]*(length_x) for i in range(length_x)]
    result = ['']*length_x

    for i in range(length_x):
        length[i][i] = 1

    for i in range(1, length_x):
        tmp = 0
        j = 0
        while j+i < length_x:       #考虑所有连续的长度为i+1的子串，该串为sequence_x[j][j+1]
            """
                解释为何这样就可以
                其实就是暴力自底向上带备注的求解x[0,1],x[1,2]...x[0,2],x[1,3]...x[0,5]
            """
            if sequence_x[j] == sequence_x[j+i]:
                tmp = length[j+1][j+i-1] + 2
                result[j] = sequence_x[j]
                result[j+i] = sequence_x[j+i]
                if i == 2:
                    for k in range(j, j+i):
                        result[k] = sequence_x[k]
            else:
                tmp = max(length[j+1][j+i], length[j][j+i-1])
            length[j][j+i] = tmp
            j += 1

    return length, ''.join(result)

def main():
    """
        Main function
    """
    sequence_x = 'charactktca'
    length, result = lps(sequence_x)
    max_len = 0
    max_index = 0
    for i in length:
        if max_len <= max(i):
            max_len = max(i)
            max_index = length.index(i)
    if max_index != 0:
        max_index -= 1
    print result[max_index:max_len+max_index]

if __name__ == '__main__':
    main()
