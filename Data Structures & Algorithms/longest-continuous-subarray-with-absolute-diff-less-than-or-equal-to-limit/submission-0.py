class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQ = deque()
        minQ = deque()
        l = 0
        ans = 0

        for r in range(len(nums)):
            while maxQ and nums[maxQ[-1]] < nums[r]:
                maxQ.pop()
            maxQ.append(r)

            while minQ and nums[minQ[-1]] > nums[r]:
                minQ.pop()
            minQ.append(r)

            while nums[maxQ[0]] - nums[minQ[0]] > limit:
                l += 1
                if maxQ[0] < l:
                    maxQ.popleft()
                if minQ[0] < l:
                    minQ.popleft()

            ans = max(r-l+1, ans)

        return ans
