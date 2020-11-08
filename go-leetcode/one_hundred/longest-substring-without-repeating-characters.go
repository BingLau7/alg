package one_hundred

import (
	"fmt"
	"math"
)

// https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

/**
0. 读题
	不含重复字符串
1. 思路
	(滑动窗口)因为是从双指针算法看过来的，所以双指针算法实际就是一个指针指向起点，另外一个往终点指，直到遇到重复的为止，用个值来记录最大值
	需要 map 判断重复数据结构
2. 算法
3. 边界
4. 总结
 */

func RunLengthOfLongestSubstring() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("bbbbbb"))
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
}

func lengthOfLongestSubstring(s string) int {
	mem := map[byte]int{}
	n := len(s)

	right, res := -1, 0

	for i := 0; i < n; i++ {
		// 移动窗口减最左边的字符
		if i != 0 {
			delete(mem, s[i-1])
		}
		// 移动右指针，并保证不重复
		for right + 1 < n && mem[s[right + 1]] == 0 {
			// 计数到目前终点子串长度
			mem[s[right + 1]]++
			right++
		}
		res = int(math.Max(float64(res), float64(right - i + 1)))
	}
	return res
}
