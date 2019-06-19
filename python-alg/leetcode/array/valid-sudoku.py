from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validate_dict = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                k = self.getIndex(i, j)
                i_s = validate_dict.setdefault(i, set())
                j_s = validate_dict.setdefault(j+9, set())
                k_s = validate_dict.setdefault(k+18, set())
                v = board[i][j]
                if v == '.':
                    continue
                if v in i_s or v in j_s or v in k_s:
                    print('set', i_s, j_s, k_s)
                    print('set in', v in i_s,  v in j_s, v in k_s)
                    print('v:', v, 'i', i, 'j', j, 'k', k)
                    return False
                i_s.add(v)
                j_s.add(v)
                k_s.add(v)
        return True

    def getIndex(self, i: int, j: int) -> int:
        if i < 3:
            if j < 3: return 0
            elif j < 6: return 1
            else: return 2
        elif i < 6:
            if j < 3: return 3
            elif j < 6: return 4
            else: return 5
        else:
            if j < 3: return 6
            elif j < 6: return 7
            else: return 8


if __name__ == '__main__':
    _input = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(_input))
