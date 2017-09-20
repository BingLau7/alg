class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [int(i) for i in str(num)]
        result = reduce(lambda x, y: x + y, nums)
        if result >= 10:
            result = self.addDigits(result)
        return result


if __name__ == '__main__':
    print Solution().addDigits(38)
