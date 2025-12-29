# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        m = 1 << (n - 1)  # 2 ** (n - 1)
        if k < m:
            return self.findKthBit(n - 1, k)
        elif k == m:
            return "1"
        else:
            ans = self.findKthBit(n - 1, m * 2 - k)
            return "0" if ans == "1" else "1"
