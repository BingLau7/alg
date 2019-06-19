from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        chr_num2 = [i for i in num2]
        chr_num2.reverse()
        total_res = []
        max_l = 0
        # [[0, 0, 16, 12, 4], [0, 20, 15, 5, 0], [8, 6, 2, 0, 0]]
        for i in range(len(chr_num2)):
            res = [0] * (len(chr_num2) - i - 1)
            res.extend(self.mul(num1, chr_num2[i]))
            res.extend([0] * i)
            total_res.append(res)
            max_l = max(max_l, len(res))

        # 结果相加，最大结果只能为 max_l + 1
        # [8, 26, 33, 17, 4]
        mid_res = [0] * max_l
        for res in total_res:
            for i in range(len(res)-1, -1, -1):
                mid_res[i] += res[i]

        mid_res.reverse()
        res = []
        for i in range(len(mid_res)):
            val = mid_res[i]
            ad_val = val // 10
            res.append(val % 10)
            if i == len(mid_res) - 1 and ad_val > 0:
                res.append(ad_val)
            elif ad_val > 0:
                mid_res[i+1] += ad_val

        res.reverse()
        # 去除首位 0
        while len(res) > 0 and res[0] == 0:
            res.pop(0)
        if not res:
            return '0'
        return ''.join([str(i) for i in res])

    # if 234 * 345, num = 234, num_sol = 5 / 4 / 3
    def mul(self, num: str, num_sol: str) -> List[int]:
        if not num:
            return [0]
        if num_sol == '0':
            return [0] * len(num)
        res = []
        n2 = ord(num_sol) - 48
        for i in range(len(num) - 1, -1, -1):
            n1 = ord(num[i]) - 48
            res.append(n1 * n2)

        res.reverse()
        return res


if __name__ == '__main__':
    print(Solution().multiply('9311', '0'))
