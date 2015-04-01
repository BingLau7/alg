#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        """
            贪心算法？先得到最大利益差值，再找到此大利益差值
            得到第一组最大利益：求最小值，然后求最小值右边最大值差，求最大值，然后求左边最小值差
            上述反例:[7, 8, 3, 6, 1, 2]
            还是贪心：算一个谷值与其最接近峰值的差，计入收益，重复进行来得到最大收益
        """
        max_profit = 0
        begin = 0   #记录谷值索引
        end = 0     #记录峰值索引
        len_prices = len(prices)
        up = False  #峰值标记
        down = False #谷值标记
        i = 1
        while i < len_prices:
            if(prices[i] > prices[i-1] and up == False): #找峰值
                begin = i - 1
                up = True
                down = False

            if(prices[i] < prices[i-1] and down == False): #找谷值
                end = i - 1
                up = False
                down = True
                max_profit += (prices[end] - prices[begin])

            i += 1

        if begin < len_prices and up == True:    #如果前面无谷值，递增中
            end = len_prices - 1
            max_profit += (prices[end] - prices[begin])

        return max_profit
