package io.github.binglau.dynamic_programming;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/restore-ip-addresses/#/description

 Given a string containing only digits, restore it by returning all possible valid IP address combinations.

 For example:
 Given "25525511135",

 return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

 */

public class RestoreIPAddresses {
    public static List<String> restoreIpAddresses(String s) {
        int sLen = s.length();
        List<String> result = new ArrayList<>();
        // 将所有情况列出，逐一判断是否合法
        for (int i = 1; i < 4 && i < sLen - 2; i++) {
            for (int j = i + 1; j < i + 4 && j < sLen - 1; j++) {
                for (int k = j + 1; k < j + 4 && k < sLen; k++) {
                    String s1 = s.substring(0, i);
                    String s2 = s.substring(i, j);
                    String s3 = s.substring(j, k);
                    String s4 = s.substring(k);
                    if (isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4))
                        result.add(s1 + "." + s2 + "." + s3 + "." + s4);
                }
            }
        }
        return result;
    }

    private static boolean isValid(String s) {
        if (s.length() > 3 || Integer.parseInt(s) > 255 || (s.charAt(0) == '0' && s.length() > 1))
            return false;
        return true;
    }

    public static void main(String[] args) {
        List<String> s = restoreIpAddresses("010010");
        System.out.println(s);
    }
}
