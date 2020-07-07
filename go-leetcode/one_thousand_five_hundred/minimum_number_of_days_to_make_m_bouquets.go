package one_thousand_five_hundred

import "fmt"

// https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/

/**
0. 读题
	0.0 m 是花束的数量，k 是一束花的数量
	0.1 k 必须是相邻的才行

1. 思路
	1.0 答案提到二分
2. 数据结构与算法
	2.0 首先分的是天数，需要找到 p 天符合要求（m 束花，没束 k 朵），其次是拆分范围，按天数最大二分，1 <= bloomDay[i] <= 10^9
3. 边界
 */

func MinDaysRun() {
	fmt.Println(minDays([]int{1000000000,1000000000}, 1, 1))
	//fmt.Println(minDays([]int{7,7,7,7,12,7,7}, 2, 3))
	//fmt.Println(minDays([]int{1,10,3,10,2}, 3, 1))
}

func minDays(bloomDay []int, m int, k int) int {
	left := 1
	right := int(1e9)
	res := -1
	for left <= right {
		mid := (left + right) / 2
		if valid(bloomDay, mid, m, k) {
			res = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return res
}

func valid(bloomDay []int, days int, m int, k int) bool {
	if m * k > len(bloomDay) {
		return false
	}
	cnt := 0
	l := 0
	for _, i := range bloomDay {
		j := i - days
		if j <= 0 {
			l++
			if l == k {
				cnt++
				l = 0
			}
		} else {
			l = 0
		}
	}
	return cnt >= m
}
