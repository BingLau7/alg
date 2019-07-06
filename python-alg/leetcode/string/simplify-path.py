class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        path_segments = path.split("/")
        res = []
        for p in path_segments:
            if not p or p == ".":
                continue
            if p == "..":
                if res:
                    res.pop()
                continue
            res.append(p)
        return "/" + "/".join(res)


if __name__ == '__main__':
    # _input = "/a//b////c/d//././/.."
    _input = "/../"
    print(Solution().simplifyPath(_input))
