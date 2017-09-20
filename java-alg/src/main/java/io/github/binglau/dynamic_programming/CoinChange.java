package io.github.binglau.dynamic_programming;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/coin-change/#/description
 *
 You are given coins of different denominations and a total amount of money amount.
 Write a function to compute the fewest number of coins that you need to make up that amount.
 If that amount of money cannot be made up by any combination of the coins, return -1.

 Example 1:
 coins = [1, 2, 5], amount = 11
 return 3 (11 = 5 + 5 + 1)

 Example 2:
 coins = [2], amount = 3
 return -1.

 Note:
 You may assume that you have an infinite number of each kind of coin.
 */

public class CoinChange {
    private static int coinChange(int[] coins, int amount){
        if (coins == null || coins.length == 0 ) return -1;
        int[] mem = new int[amount + 1];
        return _coinChange(coins, amount, mem);
    }

    // 动态规划，mem记录可以解决的价格, mem[rem]记录解决这个rem需要多少coin
    private static int _coinChange(int[] coins, int rem, int[] mem) {
        if (rem < 0) return -1;
        if (rem == 0) return 0; // 问题结束
        if (mem[rem] != 0) return mem[rem];
        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int result = _coinChange(coins, rem-coin, mem);
            if (result >= 0 && result < min)
                min = result + 1;
        }
        mem[rem] = (min == Integer.MAX_VALUE) ? -1 : min;
        return mem[rem];
    }

    private static int coinChangeIterative(int[] coins, int amount){
        int[] mem = new int[amount + 1]; // mem[i] 表示 i 的和需要的最小次数
        int sum = 0;
        while (++sum <= amount) {
            int min = -1;
            for (int coin : coins) {
                if (sum >= coin && mem[sum - coin] != -1) {
                    int res = mem[sum - coin] + 1;
                    if (min < 0) min = res;
                    else min = res < min ? res : min;
                }
            }
            mem[sum] = min;
        }
        return mem[amount];
    }

    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;
        System.out.println(coinChangeIterative(coins, amount));
    }
}
