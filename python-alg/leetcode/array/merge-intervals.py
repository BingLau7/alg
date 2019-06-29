from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) < 2:
            return intervals

        # 先对数组进行排序，排序以第一个元素为准
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]

        for l in sorted_intervals:
            process_l = res.pop()
            before = process_l
            after = l
            # 若前者最后一位包含了后者，以后者为准，意味着要合并
            # 两者前后没有直接的大小顺序关系，先需要确定二者关系
            if after[0] <= before[1] <= after[1]:
                after[0] = min(after[0], before[0])
                after[1] = max(after[1], before[1])
            elif before[1] >= after[1]: # 前面的包含后面的情况
                after = before
            else:
                res.append(before)
            res.append(after)
        return res


if __name__ == '__main__':
    # _input = [[1, 4], [4, 5]]
    # _input = [[1,3],[2,6],[8,10],[15,18]]
    # _input = [[1, 4], [0, 0]]
    # _input = [[1, 4], [0, 1]]
    # _input = [[1,4],[2,3]]
    _input = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(Solution().merge(_input))
