package two_hundred

import (
	"fmt"
	"math"
)

// https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/

func RunTowSum() {
	fmt.Println(twoSum([]int{3,24,50,79,88,150,345}, 200))
}

/**
0. 读题
	0. 有序
	1. 两个数
	2. 假设只有一个答案
	3. 返回坐标不是从 0 开始的
1. 思路
	0. 有序使用二分
	1. 两个数，首先先减去 nums[i] 的数，则变成在 i - n 中查找是否有符合的数字，标准二分
2. 算法
	0. 二分
3. 边界
4. 总结
 */
func twoSum(numbers []int, target int) []int {
	if len(numbers) < 2 {
		return nil
	}
	for i := 0; i < len(numbers); i++ {
		tar := target - numbers[i]
		right := len(numbers) - 1
		left := i + 1
		for left <= right {
			mid := int(math.Ceil(float64(left + right) / 2))
			if tar == numbers[mid] {
				return []int{i + 1, mid + 1}
			} else if tar < numbers[mid]  {
				right = mid - 1
			} else {
				if left == right {
					break
				}
				left = mid
			}
		}
	}
	return nil
}

// 答案中提到的双指针解法

/**
初始时两个指针分别指向第一个元素位置和最后一个元素的位置。每次计算两个指针指向的两个元素之和，并和目标值比较。
如果两个元素之和等于目标值，则发现了唯一解。
如果两个元素之和小于目标值，则将左侧指针右移一位。
如果两个元素之和大于目标值，则将右侧指针左移一位。
移动指针之后，重复上述操作，直到找到答案。
 */
func twoSumDoublePoint(numbers []int, target int) []int {
	low, high := 0, len(numbers) - 1
	for low < high {
		sum := numbers[low] + numbers[high]
		if sum == target {
			return []int{low + 1, high + 1}
		} else if sum < target {
			low++
		} else {
			high--
		}
	}
	return []int{-1, -1}
}

