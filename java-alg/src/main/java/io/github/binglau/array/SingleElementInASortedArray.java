package io.github.binglau.array;

/**
 * https://leetcode.com/problems/single-element-in-a-sorted-array/#/description
 *
 Given a sorted array consisting of only integers where every element appears twice except for one
 element which appears once. Find this single element that appears only once.

 Example 1:
 Input: [1,1,2,3,3,4,4,8,8]
 Output: 2

 Example 2:
 Input: [3,3,7,7,10,11,11]
 Output: 10

 Note: Your solution should run in O(log n) time and O(1) space.

 */
public class SingleElementInASortedArray {
    public static int singleNonDuplicate(int[] nums) {
        if (nums.length == 1) return nums[0];
        // 第一个出现不等的情况
        if (nums.length >= 3) {
            if ((nums[0] ^ nums[1]) !=0 && (nums[1] ^ nums[2]) == 0) return nums[0];
        }
        for (int i = 1; i < nums.length - 1; i++) {
            if ((nums[i-1] ^ nums[i]) != 0 && (nums[i] ^ nums[i+1]) != 0) return nums[i];
        }
        return nums[nums.length - 1];
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 2, 2, 4, 4, 5, 5, 9};
        System.out.println(singleNonDuplicate(nums));
    }
}
