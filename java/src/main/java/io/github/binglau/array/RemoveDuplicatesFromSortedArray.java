package io.github.binglau.array;

/**
 * 文件描述:
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description
 *

 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

 Do not allocate extra space for another array, you must do this in place with constant memory.

 For example,
 Given input array nums = [1,1,2],

 Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
 */

public class RemoveDuplicatesFromSortedArray {
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int result = 0, curNum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (curNum != nums[i]) result++;
            curNum = nums[i];
            nums[result] = nums[i];
        }
        return result + 1;
    }

    public static void main(String[] args) {
        System.out.println(removeDuplicates(new int[]{1, 1, 2}));
    }
}
