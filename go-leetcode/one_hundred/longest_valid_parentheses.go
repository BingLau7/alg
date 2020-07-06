package one_hundred

import (
	"fmt"
	"go-leetcode/base"
)

// https://leetcode-cn.com/problems/longest-valid-parentheses/

/**
说明：

0. 读题
	0.0 只包含 '(' 与 ')'
	0.1 最长有效括号长度是只从 0 开始，若遇到有效括号则 +2，最长的

1. 使用什么样的数据结构
	stack

2. 思路
	2.1 创建与字符串相同 int 数组
    2.2 将 '(' 位置置为 1
    2.3 若成功匹配 ')' 将其位置与之前**不为 0 位置**置为 0
    2.4 计算数组连续 0 最长长度

3. 边界条件是什么
	3.1 对于 '()()' 结果数组全为 0 通过 1 来判断最长边界会出现分支，这个时候比较好的做法是强行在末尾添加个 1 避免该情况
    3.2 对于 '(())' 结果消耗外部括号的时候将前面置为 0 需要考虑找到没有被消耗的 '('
 */

func LongestValidParenthesesRun() {
	fmt.Println(longestValidParentheses("()(())"))
	fmt.Println(longestValidParentheses("()(()"))
	fmt.Println(longestValidParentheses("()()"))
	fmt.Println(longestValidParentheses("(()"))
	fmt.Println(longestValidParentheses(")()())"))
}

func longestValidParentheses(s string) int {
	resArr := make([]int, len(s))
	var stack base.Stack
	stack = []string{}
	for i := 0; i < len(s); i++ {
		r := string(s[i])
		consume(&stack, r, resArr, i)
	}
	resArr = append(resArr, 1)
	res := 0
	j := 0
	for i := 0; i < len(resArr); i++ {
		if resArr[i] == 1 {
			if res < (i - j) {
				res = i - j
			}
			j = i + 1
		}
	}
	return res
}

func consume(stack *base.Stack, c string, resArr []int, i int) {
	if stack.IsEmpty() {
		stack.Push(c)
		resArr[i] = 1
		return
	}

	if c == ")" {
		b, _ := stack.Pop()
		if b == "(" {
			resArr[i] = 0
			for j := i; j >= 0; j-- {
				if resArr[j] == 1 {
					resArr[j] = 0
					break
				}
			}
		} else {
			stack.Clean()
			resArr[i] = 1
		}
	} else {
		resArr[i] = 1
		stack.Push(c)
	}
}