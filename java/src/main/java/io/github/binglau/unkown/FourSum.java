package io.github.binglau.unkown;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * https://leetcode.com/problems/4sum/#/description
 *
 Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

 Note: The solution set must not contain duplicate quadruplets.

 For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

 A solution set is:
 [
 [-1,  0, 0, 1],
 [-2, -1, 1, 2],
 [-2,  0, 0, 2]
 ]
 */
public class FourSum {
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                for (int j = i + 1; j < nums.length - 2; j++) {
                    if (j == i + 1 || (j > 0 && nums[j] != nums[j - 1])) {
                        int lo = j + 1, hi = nums.length - 1;
                        while (lo < hi) {
                            int sum = nums[i] + nums[j] + nums[lo] + nums[hi];
                            if (sum == target) {
                                result.add(Arrays.asList(nums[i], nums[j], nums[lo], nums[hi]));
                                while (lo < hi && nums[lo] == nums[lo + 1]) lo++;
                                while (lo < hi && nums[hi] == nums[hi - 1]) hi--;
                                lo++;
                                hi--;
                            } else if (sum < target) lo++;
                            else hi--;
                        }
                    }
                }
            }
        }
        return result;
    }


    public static void main(String[] args) {
        int[] nums = {0, 0, 0, 0};
        System.out.println(fourSum(nums, 0));
    }
}
