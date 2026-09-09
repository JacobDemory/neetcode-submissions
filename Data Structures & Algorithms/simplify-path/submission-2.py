class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        groups = path.split('/')
        for s in groups:
            if s == '..':
                if ans:
                    ans.pop()
            elif s and s != '.':
                ans.append(s)
        return '/' + '/'.join(ans)