package io.github.binglau.unkown;

import java.util.Arrays;

/**
 *
 */
public class ThreeSumClosest {
    public static int threeSumClosest(int[] nums, int target) {
        int result = nums[0] + nums[1] + nums[2];
        Arrays.sort(nums);
        // 排除第一个元素，使用 2sum 方法
        for (int i = 0; i < nums.length - 2; i++) {
                int lo = i + 1, hi = nums.length - 1;
                while (lo < hi) {
                    int sum = nums[i] + nums[lo] + nums[hi];
                    if (sum > target) hi--;
                    else lo++;
                    if (Math.abs(sum - target) < Math.abs(result - target)) result = sum;
                }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 0};
        System.out.println(threeSumClosest(nums, -100));
    }
}
