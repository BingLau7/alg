package io.github.binglau.dynamic_programming;

public class LCS {

    private static int longestCommonSubSequenceDP(String a, String b) {
        if (a == null || b == null) {
            return 0;
        }

        int aLen = a.length();
        int bLen = b.length();
        // 为什么要大一维? 因为当算式是需要 - 1 的，i == j == 0 时候也就是初始时候需要 上面一个是 0
        int[][] memo = new int[aLen + 1][bLen + 1];
        for (int i = 0; i <= aLen; i++) {
            memo[i][0] = 0;
        }
        for (int j = 0; j <= bLen; j++) {
            memo[0][j] = 0;
        }

        for (int i = 1; i <= aLen; i++) {
            for (int j = 1; j <= bLen; j++) {
                // c[i, j] = c[i - 1, j - 1] + 1 if i,j > 0 and xi = yj
                if (a.charAt(i - 1) == b.charAt(j - 1)) {
                    memo[i][j] = memo[i - 1][j - 1] + 1;
                // c[i, j] = max(c[i, j - 1], c[i - 1, j]) if i,j > 0 and xi != yj
                } else {
                    memo[i][j] = Math.max(memo[i - 1][j], memo[i][j - 1]);
                }
            }
        }

        /*
        System.out.println("    " + Arrays.toString(b.toCharArray()));
        for (int idx = 0; idx < memo.length; idx++) {
            System.out.println((idx == 0 ? " " : a.charAt(idx - 1)) + Arrays.toString(memo[idx]));
        }
        */

        // print longest common sub sequence
        System.out.println(backtrack(memo, a, b, a.length(), b.length()));

        return memo[aLen][bLen];
    }

    // 回溯方法找路径，不断往左，上爬
    /*
        [x, j, k, c, d, e, a, l, c, e, f, g, k]
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    b[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    c[0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    d[0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    e[0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3]
    f[0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4]
    g[0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 5, 5]
     */
    private static String backtrack(int[][] memo, String a, String b, int i, int j) {
        if (i == 0 || j == 0) {
            return "";
        } else if (a.charAt(i - 1) == b.charAt(j - 1)) {
            // 走↖️
            return backtrack(memo, a, b, i - 1, j - 1) + a.charAt(i - 1);
        } else if (memo[i][j - 1] > memo[i - 1][j]) {
            // 走←
            return backtrack(memo, a, b, i, j - 1);
        } else {
            // 走↑
            return backtrack(memo, a, b, i - 1, j);
        }
    }

    public static void main(String[] args) {
        String a = "abcdefg";
        String b = "xjkcdealcefgk";
        longestCommonSubSequenceDP(a, b);
    }

}
