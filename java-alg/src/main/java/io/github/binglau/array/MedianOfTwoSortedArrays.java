package io.github.binglau.array;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/median-of-two-sorted-arrays/#/description
 *
 There are two sorted arrays nums1 and nums2 of size m and n respectively.

 Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

 Example 1:
 nums1 = [1, 3]
 nums2 = [2]

 The median is 2.0

 Example 2:
 nums1 = [1, 2]
 nums2 = [3, 4]

 The median is (2 + 3)/2 = 2.5
 */
public class MedianOfTwoSortedArrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 获得中位数所在位置，这里的位置 1 就是指第一个元素
        // 如果是和为单数，则 l == r，否则 l = r - 1
        int l = (nums1.length + nums2.length + 1) / 2;
        int r = (nums1.length + nums2.length + 2) / 2;

        // return (getkth(nums1, 0, nums2, 0, l) + getkth(nums1, 0, nums2, 0, r)) / 2.0;
        return (getkth(nums1, nums2, l - 1) + getkth(nums1, nums2, r - 1)) / 2;

    }

    // 获得 nums1 与 nums2 集合而成的数组中的第 k 个值
    private static double getkth(int nums1[], int num1Start, int nums2[], int num2Start, int k) {
        // 只有 nums2, 获取 nums2 的第 k 个数组（从start开始数）
        if (num1Start > nums1.length - 1) return nums2[num2Start + k - 1];
        // 同上
        if (num2Start > nums2.length - 1) return nums1[num1Start + k - 1];

        if (k == 1) return Math.min(nums1[num1Start], nums2[num2Start]);

        // num1Mid 与 num2Mid 均代表，k 所在的值无论是在哪个数组中，都只能在这两个数组之后，这样就可以渐渐逼近
        int num1Mid = Integer.MAX_VALUE, num2Mid = Integer.MAX_VALUE;
        if (num1Start + k / 2 - 1 < nums1.length) num1Mid = nums1[num1Start + k / 2 - 1];
        if (num2Start + k / 2 - 1 < nums2.length) num2Mid = nums2[num2Start + k / 2 - 1];

        // 当 num1Mid < num2Mid 时，num1Mid 的元素先进入大数组中（概念中），则下一步从 num1Start + k / 2 开始逼近
        if (num1Mid < num2Mid) return getkth(nums1, num1Start + k / 2, nums2, num2Start, k - k / 2);
        // 同上类推
        else return getkth(nums1, num1Start, nums2, num2Start + k / 2, k - k / 2);
    }

    // 获得 nums1 与 nums2 集合而成的数组中的第 k 个值， 这里的 k 从 0 开始
    private static double getkth(int nums1[], int nums2[], int k) {
        // 确保 nums 1是比较小的数组
        if (nums1.length > nums2.length) return getkth(nums2, nums1, k);
        if (nums1.length == 0) return nums2[k];
        int i = 0, j = 0;
        if (k == 0) return Math.min(nums1[0], nums2[0]);
        if (k == nums1.length + nums2.length - 1) return Math.max(nums1[nums1.length - 1], nums2[nums2.length - 1]);
        for (; i < nums1.length;) {
            // nums1的数组进入大数组中
            if (nums1[i] <= nums2[j]) {
                if (i + j == k) {
                    return nums1[i];
                }
                // 如果 i 不是在 k 位置则指针移动
                i++;
            } else {
                if (i + j == k) {
                    return nums2[j];
                }
                // 如果 j 不是在 k 位置则指针移动
                j++;
                // 处理 j 超界的情况, 这种情况只能在 nums1.length == nums2.length && k == nums1.length
                if (j == nums2.length && k == nums2.length && nums1.length == nums2.length)
                    return nums1[i];
            }
        }

        // 循环完 nums1 之后没有找到能返回的，则nums1.length 元素已经走过了，则只有 nums2 有元素，则看距离 k 还有多少个值 == k - i
        return nums2[k - i];
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        System.out.println(getkth(nums1, nums2, 2));
//        System.out.println(findMedianSortedArrays(nums1, nums2));
    }
}
