package io.github.binglau.dynamic_programming;

/**
 * 类MaximumSubarray.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-11-27 下午3:36
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
        int[] nums = {1, -2, 3, 10, -4, 7, 2, -5};
        int result = maxSubArray(nums);
        System.out.println(result);
    }
}
