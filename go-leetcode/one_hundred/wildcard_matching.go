package one_hundred

import "fmt"

// https://leetcode-cn.com/problems/wildcard-matching/

/**
说明:

0. 读题
	0.0 只有 * 与 ?，通配符匹配

1. 数据结构、算法
	1.0 动态规划

2. 思路
	2.0 dp[i][j]表示s到i位置,p到j位置是否匹配!
    2.1 初始化:
		dp[0][0]:什么都没有,所以为true
		第一行dp[0][j],换句话说,s为空,与p匹配,所以只要p开始为*才为true
		第一列dp[i][0],当然全部为False
	2.2 动态方程:
    	如果(s[i] == p[j] || p[j] == "?") && dp[i-1][j-1] ,有dp[i][j] = true
		如果p[j] == "*" && (dp[i-1][j] = true || dp[i][j-1] = true) 有dp[i][j] = true
 			dp[i][j-1],表示*代表是空字符,例如ab,ab*
​ 			dp[i-1][j],表示*代表非空任何字符,例如abcd,ab* # 附上自顶向下方法

3. 边界
 */


func IsMatchRun() {
	fmt.Println(isMatch("zacabz", "*a?b*"))
	//fmt.Println(isMatch("aa", "a"))
	//fmt.Println(isMatch("aa", "*"))
	//fmt.Println(isMatch("cb", "?a"))
	//fmt.Println(isMatch("adceb", "*a*b"))
	//fmt.Println(isMatch("acdcb", "a*c?b"))
}

func isMatch(s string, p string) bool {
	// 0. 初始化
	sLen := len(s)
	pLen := len(p)
	var dp [][]bool
	for i := 0; i <= sLen; i++ {
		pArr := make([]bool, 0, pLen)
		for j := 0; j <= pLen; j++ {
			pArr = append(pArr, false)
		}
		dp = append(dp, pArr)
	}
	dp[0][0] = true
	for j := 1; j <= pLen; j++ {
		if string(p[j-1]) == "*" {
			dp[0][j] = dp[0][j - 1]
		}
	}

	for i := 1; i <= sLen; i++ {
		sChar := string(s[i - 1])
		for j := 1; j <= pLen; j++ {
			pChar := string(p[j - 1])
			// ? 的匹配
			if (sChar == pChar || pChar == "?") && dp[i-1][j-1] {
				dp[i][j] = true
			} else if pChar == "*" && (dp[i-1][j] || dp[i][j-1]) {
				dp[i][j] = true
			}
		}
	}
	return dp[sLen][pLen]
}