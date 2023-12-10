class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path = {}
        for path in paths:
            path_l = path.split()
            # print(path_l)
            base = path_l[0]
            for filee in path_l[1:]:
                # print(filee)
                idx =  filee.index("(")
                idxx = filee.index(")")
                content = filee[idx + 1 : idxx]
                arr = content_path.get(content, [])
                arr.append(base + '/' + filee[: idx])
                content_path[content] = arr
        ans = []

        # print(content_path)
        for key in content_path:
            if len(content_path[key]) > 1:
                ans.append(content_path[key])
        return ans






        