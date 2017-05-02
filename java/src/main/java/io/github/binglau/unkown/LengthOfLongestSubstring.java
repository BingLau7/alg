package io.github.binglau.unkown;


import java.util.Collections;
import java.util.HashMap;

/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
 *
 Given a string, find the length of the longest substring without repeating characters.

 Examples:

 Given "abcabcbb", the answer is "abc", which the length is 3.

 Given "bbbbb", the answer is "b", with the length of 1.

 Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */
public class LengthOfLongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        int result = 0;
        HashMap<Character, Integer> noRepeatChars = new HashMap<>();
        for (int i = 0, j = 0; i < s.length(); i++) {
            // 获得重复字符的下一个字符索引
            if (noRepeatChars.containsKey(s.charAt(i))) j = Math.max(j, noRepeatChars.get(s.charAt(i)) + 1);
            noRepeatChars.put(s.charAt(i), i);
            // 当前不重复子字符串大小为 i - j + 1
            result = Math.max(result, i - j + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb"));
    }
}
