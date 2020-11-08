package one_hundred

import "fmt"

// 太绕了，未完成
// https://leetcode-cn.com/problems/insert-interval/

func RunInsert() {
	// fmt.Println(insert([][]int{{1, 3}, {6, 9}}, []int{2, 5}))
	fmt.Println(insert([][]int{{1, 3}, {6, 9}}, []int{2, 5}))
}

/**
0. 读题
1. 思路
	莽过去
	1. new[1] < intervals[0] 则是加入到第一个组
	2. new[0], intervals[0], new[1], intervals[1]
	3. intervals[0], new[0], new[1], intervals[1]
	4. intervals[0], new[0], intervals[1], new[1]

	官方思路：https://leetcode-cn.com/problems/insert-interval/solution/cha-ru-qu-jian-by-leetcode/
2. 算法
3. 边界
4. 总结
 */
func insert(intervals [][]int, newInterval []int) [][]int {
	var res [][]int
	if len(intervals) == 0 && len(newInterval) != 0 {
		res = append(res, newInterval)
		return res
	}
	if len(intervals) == 0 {
		return res
	}
	for _,inner := range intervals {
		// 完全被包含的忽略
		if inner[0] > newInterval[0] && inner[1] < newInterval[1] {
			continue
		}
		// 没有交集
		if inner[1] < newInterval[0] {
			res = append(res, inner)
			continue
		}
		if inner[0] <= newInterval[0] { // 左侧场景
			if inner[1] > newInterval[1] { // newInterval 没有超出 inner 范围
				res = append(res, inner)
			} else { // newInterval 超出
				res = append(res, []int{inner[0], newInterval[1]})
			}
		} else { // 右侧场景
			if inner[0] > newInterval[1] { // newInterval 没有超出 inner 范围
				res = append(res, inner)
			} else if inner[1] > newInterval[1] { // 左侧交集
				if len(res) == 0 {
					res = append(res, []int{newInterval[0], inner[1]})
				} else {
					res[len(res) - 1][1] = inner[1]
				}
			} else { // inner 被覆盖则不操作
			}
		}
	}
	if res[len(res) - 1][1] < newInterval[0] {
		res = append(res, newInterval)
	}
	if res[len(res) - 1][0] > newInterval[1] {
		index := len(res) - 1
		rear := append([][]int{}, res[:index + 1]...)
		res = append(res[0:index], newInterval)
		res = append(res, rear...)
	}
	return res
}
