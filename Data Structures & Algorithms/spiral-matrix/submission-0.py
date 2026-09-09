class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while len(ans) < len(matrix) * len(matrix[0]):
            for i in range(l, r+1):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t, b+1):
                ans.append(matrix[i][r])
            r -= 1
            if t > b or l > r:
                break
            for i in range(r, l-1, -1):
                ans.append(matrix[b][i])
            b -= 1
            for i in range(b, t-1, -1):
                ans.append(matrix[i][l])
            l += 1
        return ans
