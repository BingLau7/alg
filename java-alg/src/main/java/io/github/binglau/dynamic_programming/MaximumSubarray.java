package io.github.binglau.dynamic_programming;

/**
 * https://leetcode.com/problems/maximum-subarray/#/description
 *
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

 For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 the contiguous subarray [4,-1,2,1] has the largest sum = 6.

 */
public class MaximumSubarray {
    public static int maxSubArray(int[] nums) {
        int result = nums[0];
        int currentSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(currentSum + nums[i], nums[i]);
            result = Math.max(currentSum, result);
        }
        return result;
    }

    public static void main(String[] args) {
//        int[] nums = {1, -2, 3, 10, -4, 7, 2, -5};
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int result = maxSubArray(nums);
        System.out.println(result);
    }
}
