package alg

import (
	"fmt"
	"utils"
)

/**
https://leetcode.com/problems/summary-ranges/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

 */
func SummaryRanges(nums []int) []string {
	numsSize := len(nums)
	var result []string
	if numsSize == 0 {
		return result
	}
	if numsSize == 1 {
		return append(result, fmt.Sprint(nums[0]))
	}
	for i := 0; i < numsSize; i++ {
		a := nums[i]
		// 循环到差值为 1 的点
		for i + 1 < numsSize && nums[i + 1] - nums[i] == 1{
			i++
		}
		// 表示前方没有连续数值
		if a == nums[i] {
			result = append(result, fmt.Sprintf("%d", a))
		} else {
			result = append(result, fmt.Sprintf("%d->%d", a, nums[i]))
		}

	}
	return result
}

/**
https://leetcode.com/problems/first-missing-positive/description/

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
 */

 /**
 1. 先将各个正数移动到数组中对应的索引处（数字 - 1 的位置），负数和大于数组长度的不移地
 2. 再遍历一遍数组找出第一个负数或者大于数组长度的数
  */
func FirstMissingPositive(nums []int) int {
	numsLen := len(nums)
	if numsLen == 0 {
		return 1
	}
	for i, num := range nums {
		if num > 0 && num <= numsLen {
			utils.SwapArrayNum(nums, i, num - 1)
		}
	}
	fmt.Println(nums)
	return 0
}
