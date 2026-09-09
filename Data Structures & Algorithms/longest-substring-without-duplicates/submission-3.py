class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in found and found[s[r]] >= l:
                l = found[s[r]] + 1
            found[s[r]] = r
            ans = max(r-l+1, ans)
        return ans
