package io.github.binglau.unkown;

import java.util.*;

/**
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description
 *
 Given a digit string, return all possible letter combinations that the number could represent.

 A mapping of digit to letters (just like on the telephone buttons) is given below.



 Input:Digit string "23"
 Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

 */
public class LetterCombinations {
    private static String[] map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    public static List<String> letterCombinations(String digits) {
        LinkedList<String> result = new LinkedList<>();
        if (digits.length() == 0) return result;
        result.add("");
        for (int i = 0; i < digits.length(); i++) {
            int index = Character.getNumericValue(digits.charAt(i));
            while (result.peek().length() == i) {
                String t = result.remove();
                for (char s : map[index].toCharArray()) result.add(t + s);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(letterCombinations("23"));
    }
}
