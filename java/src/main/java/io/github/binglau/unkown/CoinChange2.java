package io.github.binglau.unkown;

import java.util.Arrays;

public class CoinChange2 {

    private static int change(int amount, int[] coins) {
        Arrays.sort(coins);
        int n = (amount / coins[0]) ;
        System.out.println(n);
//        for (int i = 0; i < n; i++) {
//
//        }
        return 0;
    }

    public static void main(String[] args) {
        int result = CoinChange2.change(5, new int[]{2, 5});
        System.out.println(result);
    }
}
