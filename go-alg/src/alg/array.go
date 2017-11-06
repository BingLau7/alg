package alg

import "fmt"

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
