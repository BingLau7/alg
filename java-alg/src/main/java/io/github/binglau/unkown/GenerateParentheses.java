package io.github.binglau.unkown;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/generate-parentheses/#/description
 *
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 For example, given n = 3, a solution set is:

 [
 "((()))",
 "(()())",
 "(())()",
 "()(())",
 "()()()"
 ]
 */

public class GenerateParentheses {
    public static List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrace(result, "", 0, 0, n);
        return result;
    }

    public static void backtrace(List<String> list, String str, int open, int close, int max) {
        if (str.length() == max * 2) {
            list.add(str);
            return;
        }

        // 利用递归，对每个 open 都有 close 往下走直到等于 max
        if (open < max) backtrace(list, str + "(", open + 1, close, max);
        if (close < open) backtrace(list, str + ")", open, close + 1, max);
    }

    public static void main(String[] args) {
        System.out.println(generateParenthesis(4));
    }
}
