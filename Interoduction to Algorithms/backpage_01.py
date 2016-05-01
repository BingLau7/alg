#coding:utf-8
"""
    0-1背包问题:num个商品，第i个商品价值value[i]，重weight[i],均为整数，
    背包只能容纳WEIGHT的商品，求最多可拿的价值及其物品，物品不可分
"""
WEIGHT = 50
INFINITY = float('inf')



def solution(weight, value, num):
    """
        解答
    """
    record = [[0]*(WEIGHT+1) for i in range(num+1)]

    for i in range(num+1):
        for now_weight in range(WEIGHT+1):
            if weight[i] > now_weight:
                record[i][now_weight] = record[i-1][now_weight]
            else:
                if record[i-1][now_weight] > record[i-1][now_weight- weight[i]] + value[i]:
                    record[i][now_weight] = record[i-1][now_weight]
                else:
                    record[i][now_weight] = record[i-1][now_weight- weight[i]] + value[i]

    left_weight = WEIGHT
    for i in range(num, 0, -1):
        if left_weight >= weight[i]:
            if (record[i][left_weight] - record[i-1][left_weight-weight[i]]) == value[i]:
                print i, 'select'
                left_weight -= weight[i]


    print record[num][WEIGHT]


def main():
    """
        Main function
    """
    weight = [0, 10, 20, 30]
    value = [0, 600, 300, 120]

    solution(weight, value, 3)

if __name__ == '__main__':
    main()
