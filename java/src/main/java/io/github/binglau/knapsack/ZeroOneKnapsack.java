package io.github.binglau.knapsack;

import java.util.Arrays;

/**
 * 有N件物品和一个容量为V的背包。第i件物品的费用是c[i], 价值是w[i]。求解将哪些物品装入背包可使价值总和最大。
 *
 * 子问题定义状态：即f[i][v]表示前i件物品恰放入一个容量为v的背包可以获得最大价值。则其状态转移方程便是:
 * f[i][v] = max(f[i-1][v], f[i-1][v-c[i]] + w[i])
 */
public class ZeroOneKnapsack {
    private int[][] f;
    private int[] c;
    private int[] w;
    private int V;
    private int N;

    public ZeroOneKnapsack(int V, int[] c, int[] w) {
        this.N = c.length;
        this.V = V;
        f = new int[N + 1][V + 1];
        this.c = c;
        this.w = w;
    }

    private void setMaxValue(int i, int v) {
        f[i][v] = Math.max(f[i-1][v], f[i-1][v-c[i]] + w[i]);
    }

    private void zeroOnePack(int cost, int weight) {
        for (int i = 1; i < V; i++) {
        }
    }

    public static void main(String[] args) {
        int[] c = new int[]{4, 3, 5, 8};
        int[] w = new int[]{4, 3, 5, 8};
        System.out.println(Arrays.toString(c));
    }
}
