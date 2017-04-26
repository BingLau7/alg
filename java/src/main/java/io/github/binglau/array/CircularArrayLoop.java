package io.github.binglau.array;

/**
 * https://leetcode.com/problems/circular-array-loop/#/description
 *
 You are given an array of positive and negative integers.
 If a number n at an index is positive, then move forward n steps.
 Conversely, if it's negative (-n), move backward n steps.
 Assume the first element of the array is forward next to the last element,
 and the last element is backward next to the first element.
 Determine if there is a loop in this array.
 A loop starts and ends at a particular index with more than 1 element along the loop.
 The loop must be "forward" or "backward'.

 Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

 Example 2: Given the array [-1, 2], there is no loop.

 Note: The given array is guaranteed to contain no element "0".

 Can you do it in O(n) time complexity and O(1) space complexity?

 解题思路：

 Start from any index, move to the next index by function
 f(i) = ((i + nums[i]) % len + len) % len where len is the length of array nums.
 and follow the chain. We are guaranteed there is a cycle in this chaining process.
 check if all the numbers in the cycle are backward or forward.
 Remember to exclude the one element cycle cases.

 Just think it as finding a loop in Linkedlist,
 except that loops with only 1 element do not count.
 Use a slow and fast pointer, slow pointer moves 1 step a time
 while fast pointer moves 2 steps a time.
 If there is a loop (fast == slow), we return true,
 else if we meet element with different directions,
 then the search fail, we set all elements along the way to 0.
 Because 0 is fail for sure so when later search meet 0 we know the search will fail.

 最后还是不懂- -

 */
public class CircularArrayLoop {
    static boolean circularArrayLoop(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        for (int a : nums) {
            if (a == 0) return false;
        }
        int len = nums.length;
        for (int i = 0; i < len; i++)
            if (checkCycle(nums, i)) return true;
        return false;
    }

    private static boolean checkCycle(int[] nums, int start) {
        int len = nums.length;
        int slow = ((start + nums[start]) % len + len) % len;
        // fast 多走一步
        int fast = ((slow + nums[slow]) % len + len) %len;
        while (slow != fast) {
            slow = ((slow + nums[slow]) % len + len) % len;
            fast = ((fast + nums[fast]) % len + len) % len;
            fast = ((fast + nums[fast]) % len + len) % len;
        }
        if (slow == ((slow + nums[slow]) % len + len) % len) return false;
        boolean forward_backward = nums[slow] > 0;
        int ptr = ((slow + nums[slow]) % len + len) % len;
        while (ptr != slow) {
            if (nums[ptr] > 0 != forward_backward) return false;
            ptr = ((ptr + nums[ptr]) % len + len) % len;
        }
        return true;
    }

    public static void main(String[] args) {
        int[] nums = {2, -1, 1, 2, 2};
        System.out.println(circularArrayLoop(nums));
    }
}
