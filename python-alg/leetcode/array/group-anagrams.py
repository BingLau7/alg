from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for v in strs:
            count = [0] * 26
            for c in v:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(v)
        return [r for r in res.values()]


if __name__ == '__main__':
    _input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(_input))
