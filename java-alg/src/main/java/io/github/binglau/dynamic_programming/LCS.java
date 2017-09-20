package io.github.binglau.dynamic_programming;

/**
 * 1. 刻画最长公共子序列的特征
 * (LCS 的最优子结构) 令 X = <x1, x2, ..., xm> 和 Y = <y1, y2, ..., yn> 为两个序列，Z = <z1, z2, ..., zk> 为 X 和 Y 的任意 LCS
 * ① 如果 x[m] = y[n], 则 z[k] = x[m] = y[n] 且 z[k-1] 是 x[m-1] 和 y[n-1] 的一个 LCS
 * ② 如果 x[m] != y[n], 那么 z[k] != x[m] 意味着 Z 是 Y[m-1] 和 Y 的一个 LCS
 * ③ 如果 x[m] = y[n]，那么 z[k] != y[n] 意味着 Z 是 X 和 Y[n-1] 的一个 LCS
 *
 * 2. 一个递归解
 *             0                                若 i = 0 或 j = 0
 * c[i, j] =   c[i - 1, j - 1] + 1              若 i,j > 0 且 x[i] = y[i]
 *             max(c[i, j - 1], c[i - 1, j])    若 i,j > 0，且 x[i] != y[j]
 *
 * 3. 计算 LCS 长度 (memo 的结果)
 * 4. 构造 LCS (backtrack 方法回溯)
 */
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
