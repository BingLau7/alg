"""
自己的解法：
1. 一个二维数组，i 表示开始, j 表示结束，[i][j] = true 表示是回文，false 表示不是
2. [i][j] = true 需要建立在 [i-1][j-1] = true 的情况

初始化：[i][j] = true if i = j - 1 or i = j else false
递增：
1. [i][j] = True 的情况下，判断 [i-1] == [j+1] ，如果相等，则 [i-1][j+1] = True
2. i 先从 1 开始
结果：挑出 true 的数组对，然后相减看范围最大
"""

class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        len_s = len(s)

        if len_s == 1:
            return s

        # init
        memory = [[False for i in range(len_s)] for i in range(len_s)]
        for i in range(len_s):
            memory[i][i] = True
            if i < len_s - 1 and s[i] == s[i+1]:
                memory[i][i+1] = True


        # 找到回文点
        for i in range(1, len_s):
            for j in range(len_s-1):
                if i > j: continue
                if memory[i][j] and s[i-1] == s[j+1]: 
                    print('1:', i-1, '-', j+1, ':', s[i-1:j+2])
                    memory[i-1][j+1] = True
                    for k in range(1, min(i-1, len_s-j)+1):
                        if j+1+k < len_s and i-1-k >= 0 and s[i-1-k] == s[j+1+k]:
                            print('2:',i-1-k, '-', j+1+k, ':', s[i-1-k:j+2+k])
                            memory[i-1-k][j+1+k] = True
                        else: break

        result = []
        for i in range(len_s):
            for j in range(len_s):
                if i > j: continue
                if memory[i][j]:
                    result.append(s[i:j+1])

        print(result)

        return max(result, key=len)

    def betterLongestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if not s:
            return s

        res = []
        for i in range(len_s):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            res.append(tmp)
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            res.append(tmp)

        # print(res)

        return max(res, key=len)
        
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

if __name__ == '__main__':
    print(Solution().betterLongestPalindrome('aaabaaaa'))