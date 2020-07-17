package two_hundred

import "fmt"

// https://leetcode-cn.com/problems/find-peak-element/

func RunFindPeakElement() {
	fmt.Println(findPeakElement([]int{1,2,3,1}))
}

/**
0. 读题
	峰值是指前后都比该值低，算法是 log(n)
1. 思路
	1.0 确定遍历是 o(n)
	1.1 最大值必然是峰值，二分找最大值
2. 算法/数据结构
	2.0 二分
3. 边界
4. 总结
 */
func findPeakElement(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	return search(nums, 0, len(nums)-1)
}


func search(nums []int, left int, right int) int {
	if left >= right {
		return left
	}
	mid := (left + right) / 2
	if mid == left {
		if nums[left] > nums[right] {
			return left
		} else {
			return right
		}
	}
	if nums[mid] < nums[mid -1] {
		return search(nums, left, mid - 1)
	}
	return search(nums, mid, right)
}
