package io.github.binglau.unkown;

/**
 * https://leetcode.com/problems/longest-palindromic-substring/#/description
 *
 Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

 Example:

 Input: "babad"

 Output: "bab"

 Note: "aba" is also a valid answer.
 Example:

 Input: "cbbd"

 Output: "bb"

 解法: https://segmentfault.com/a/1190000003914228
 */
public class LongestPalindromicSubstring {
    public static String longestPalindrome(String s) {
//        return checkAllSubstring(s);
        return advance(s);
    }

    // 网上的方法，能理解，动态规划
    // https://discuss.leetcode.com/topic/25500/share-my-java-solution-using-dynamic-programming/2
    private static String advance(String s) {
        int n = s.length();
        if (n < 2) return s;
        int maxLen = 0;
        int minStart = 0;
        int maxEnd = 0;

        boolean[][] dp = new boolean[n][n];

        for (int i = n - 1; i >= 0; i--) { // 定义起点
            int end = i;
            for (int j = i; j < n; j++) { // 由 j 位置试到终点, 最后 j 为 true 的最大位置就是 i - j 范围内的最大回文
                dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);

                if (dp[i][j]) end = j;
            }

            if (end - i + 1 > maxLen) {
                maxLen = end - i + 1;
                minStart = i;
                maxEnd = end;
            }
        }

        return s.substring(minStart, maxEnd + 1);
    }

    private static String manacher(String s) {
        if (s.length() < 1) return s;
        String result = null;
        s = preprocess(s);
        // 看不懂- -

        return result;
    }

    private static String preprocess(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            result.append('#');
            result.append(s.charAt(i));
        }
        return result.toString();
    }


    // 方法超时
    private static String checkAllSubstring(String s) {
        if (s.length() == 0) return "";
        String result = s.substring(0, 1);
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j <= s.length(); j++) {
                String subString = s.substring(i, j);
                if (subString.length() > result.length() && checkSubstring(subString)) result = subString;
            }
        }
        return result;
    }

    private static boolean checkSubstring(String s) {
        boolean isEven = s.length() % 2 == 0;
        if (isEven) {
            // 偶数则是两个指针从中间开始移动
            for (int i = s.length() / 2, j = s.length() / 2 - 1; i < s.length(); i++, j--) {
                if (s.charAt(i) != s.charAt(j)) return false;
            }
        } else {
            // 单数则是两个指针从中间的两边开始移动
            for (int i = s.length() / 2 - 1, j = s.length() / 2 + 1; i < s.length(); i++, j--) {
                if (s.charAt(i) != s.charAt(j)) return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(longestPalindrome("ababb"));
    }
}
