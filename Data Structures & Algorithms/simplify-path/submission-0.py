class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        groups = path.split('/')
        for s in groups:
            if s == '..' and ans:
                ans.pop()
            if s != '' and s != '.' and s != '..':
                ans.append(s)
        return '/' + '/'.join(ans)