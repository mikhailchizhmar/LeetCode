# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        m = 1 << (n - 2)  # 2 ** (n - 2)
        if k <= m:
            return self.kthGrammar(n - 1, k)
        else:
            return self.kthGrammar(n - 1, k - m) ^ 1
