package io.github.binglau.unkown;

/**
 * https://leetcode.com/problems/container-with-most-water/#/description
 *
 Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.

 Note: You may not slant the container and n is at least 2.

 由于是水进去，所以虽然它是梯形，但是也要计算的是最低的那条高围成的长方形
 假设两点是 i j，则计算公式为 Min(ai, aj) * |j - i|

 左右移动两个指针，记录最大值，移动左右两边中较小的那边，期待找到一条较长的边然后其容积大于当前的最大值

 */
public class ContainerWithMostWater {
    public static int maxArea(int[] height) {
        int maxArea = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            maxArea = Math.max(maxArea, Math.min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) i++;
            else j--;
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[] height = {1, 2};
        System.out.println(maxArea(height));
    }
}
