package four_hundred

import (
	"fmt"
	"go-leetcode/base"
	"math"
	"sort"
)

// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/

/**
0. 读题
	0.0 感觉是简单的数数，并没有要求时间复杂度
	0.1 看到解题思路发现使用到了树状数组解决
1. 思路
	1.0 n^2 的时间复杂度
	1.1 题解中的树状数组
	1.2 二分查找，从右向左遍历数组，将遍历过的数字维护到有序数组中，用二分查找的方式找到插入位置，也就是比当前数小的个数。
2. 数据结构
3. 边界
	3.0 二分查找的做法在 15 个白盒测试时候失败，原因不明，数据太多无法 debug
4. 总结

 */

func RunCountSmaller() {
	fmt.Println(countSmallerWithFenwichTree([]int{5,2,6,1}))
}

func countSmallerWithFenwichTree(nums []int) []int {
	resultList := []int{}
	// 离散化
	a := discretization(nums)
	tree := base.NewFenwickTree(len(nums))
	for i := len(nums) - 1; i >= 0; i-- {
		id := sort.SearchInts(a, nums[i]) + 1
		resultList = append(resultList, tree.Query(id - 1))
		tree.Update(id, 1)
	}
	for i := 0; i < len(resultList)/2; i++ {
		resultList[i], resultList[len(resultList)-1-i] = resultList[len(resultList)-1-i], resultList[i]
	}
	return resultList
}

func discretization(nums []int) []int {
	set := map[int]struct{}{}
	for _, num := range nums {
		set[num] = struct{}{}
	}
	a := make([]int, 0, len(nums))
	for num := range set {
		a = append(a, num)
	}
	sort.Ints(a)
	return a
}

func countSmaller(nums []int) []int {
	nL := len(nums)
	var res []int
	var sortNums []int
	for i:= nL - 1; i >=0; i-- {
		idx := returnBisectLeftIndex(sortNums, nums[i])
		res = append(res, idx)
		rear:=append([]int{},sortNums[idx:]...)
		sortNums = append(sortNums[0:idx], nums[i])
		sortNums = append(sortNums, rear...)
	}
	return base.ReverseInt(res)
}

func returnBisectLeftIndex(nums []int, val int) int {
	if nums == nil || len(nums) == 0 {
		return 0
	}
	left, mid, right := 0, 0, len(nums)-1
	for {
		mid = int(math.Floor(float64((left + right) / 2)))
		if nums[mid] > val {
			right = mid - 1
		} else if nums[mid] < val {
			left = mid + 1
		} else {
			break
		}
		if left > right {
			mid = left
			break
		}
	}
	return mid
}
