package alg

import "sort"

/**
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
 */

func CombinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	var result [][] int
	combinationSum(candidates, target, [] int{}, 0, &result)
	return result
}

/**
1. 最小解空间: target - candidate == 0
2. 怎么减少 candidates: target < candidate, 则表示该 candidate 不被需要
3. 不断添加结果到 result 中
 */
func combinationSum(candidates []int, target int, cur []int, start int, result *[][]int) {
	if target == 0 {
		r := make([]int, len(cur))
		copy(r, cur)
		*result = append(*result, r)
	} else {
		for i := start; i < len(candidates) && target >= candidates[i]; i++ {
			curr := append(cur, candidates[i])
			combinationSum(candidates, target - candidates[i], curr, i, result)
		}
	}
}
