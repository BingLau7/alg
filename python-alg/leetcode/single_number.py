class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result = result ^ i
        return result


if __name__ == '__main__':
    arr = [1, 1, 3, 4, 6, 4, 3, 7, 6]
    print(Solution().singleNumber(arr))


