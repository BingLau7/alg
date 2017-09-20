package io.github.binglau.dynamic_programming;

/**
 * 类BestTimeToBuyAndSellStock.java的实现描述：TODO:类实现描述
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 *
 * @author bingjian.lbj 2016-11-27 下午1:42
 */
public class BestTimeToBuyAndSellStock {
    public static int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price: prices) {
            min = Math.min(price, min);
            maxProfit = Math.max(price-min, maxProfit);
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        int[] prices = {3, 4, 5, 6, 7};
//        int[] prices = {7, 6, 5, 4, 3};
        int result = maxProfit(prices);
        System.out.println(result);
    }
}
